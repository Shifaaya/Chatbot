from pyexpat.errors import messages

from django.shortcuts import render
from django.http import JsonResponse

from .model import chatbot
from django.views.decorators.http import require_POST
import time

from .knowledge_base import find_faq

def chat_page(request):
    return render(request, "chat/index.html")


def chat_response(request):
    user_message = request.GET.get("message", "")

    if not user_message:
        return JsonResponse({
            "error": "Please provide a message."
        }, status=400)

    messages = request.session.get("messages", [])

    if not messages:
        messages.append({
            "role": "system",
            "content": (
                "You are a friendly and helpful chatbot. "
                "Use the conversation history to answer questions. "
                "Remember facts the user has shared in earlier messages. "
                "If the user asks about their name, interests, or preferences, "
                "look at their previous messages and answer based on them. "
                "Do not claim that you do not know something if it was "
                "already stated in the conversation. "
                "Never invent personal facts that the user has not shared."
            )
        })

    print("SESSION KEY:", request.session.session_key, flush=True)
    print("HISTORY BEFORE:", messages, flush=True)

    messages.append({
        "role": "user",
        "content": user_message,
    })

    start_time = time.perf_counter()

    faq_answer = find_faq(user_message)

    if faq_answer is not None:
        response = faq_answer
        print("Response source: FAQ", flush=True)
    else:
        prompt_messages = [messages[0], messages[-1]]

        result = chatbot(
            prompt_messages,
            max_new_tokens=20,
            do_sample=False,
        )

        response = result[0]["generated_text"][-1]["content"]
        print("Response source: Qwen", flush=True)

    elapsed = time.perf_counter() - start_time

    print(
        f"Total response generation took {elapsed:.2f} seconds",
        flush=True,
    )

    messages.append({
        "role": "assistant",
        "content": response,
    })

    request.session["messages"] = messages
    print("HISTORY AFTER:", messages, flush=True)

    return JsonResponse({
        "message": response
    })


@require_POST
def clear_chat(request):
    request.session.pop("messages", None)

    return JsonResponse({
        "message": "Chat cleared successfully."
    })