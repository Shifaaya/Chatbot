
FAQS = [
    {
        "question": "What does your company do?",
        "answer": (
            "We are a Governance, Risk, and Compliance (GRC) "
            "company that helps organizations improve their "
            "governance processes, manage risks, and meet "
            "compliance requirements."
        ),
    },
    {
        "question": "What services do you offer?",
        "answer": (
            "Our services include internal audit support, "
            "risk assessments, compliance management, "
            "control reviews, and policy documentation."
        ),
    },
    {
        "question": "What is GRC?",
        "answer": (
            "GRC stands for Governance, Risk, and Compliance. "
            "It is an approach that helps organizations align "
            "their objectives, manage risks, and meet applicable "
            "requirements."
        ),
    },
    {
        "question": "Do you provide audit support?",
        "answer": (
            "Yes. We provide internal audit support, including "
            "audit planning, evidence documentation, findings "
            "tracking, and corrective-action follow-up."
        ),
    },
    {
        "question": "Do you help with risk assessments?",
        "answer": (
            "Yes. We help organizations identify risks, assess "
            "their potential impact, document risk ratings, "
            "and plan risk mitigation measures."
        ),
    },
    {
        "question": "What is compliance management?",
        "answer": (
            "Compliance management involves identifying applicable "
            "requirements, maintaining appropriate controls, "
            "monitoring compliance, and addressing identified gaps."
        ),
    },
    {
        "question": "How can I contact your company?",
        "answer": (
            "Please visit our Contact Us page or submit an enquiry "
            "through our website to reach our team."
        ),
    },
    {
        "question": "How can I request a consultation?",
        "answer": (
            "You can submit a consultation request through our "
            "website's contact form. Our team can then follow up "
            "to understand your organization's needs."
        ),
    },
    {
        "question": "Who can use your services?",
        "answer": (
            "Our services are intended for organizations that "
            "want support with governance, risk management, "
            "internal audits, and compliance processes."
        ),
    },
    {
        "question": "Does your company provide customized solutions?",
        "answer": (
            "Yes. Our services can be tailored to an organization's "
            "requirements, existing processes, and business needs."
        ),
    },
]


def find_faq(user_message):
    user_message = user_message.lower().strip()

    for faq in FAQS:
        question = faq["question"].lower()

        if user_message == question:
            return faq["answer"]

    return None

