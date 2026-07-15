from langchain_core.tools import tool


@tool
def log_interaction(message: str):
    """
    Extract interaction details from natural language.
    """
    return {
        "action": "log_interaction",
        "message": message,
    }


@tool
def edit_interaction(message: str):
    """
    Edit an existing interaction.
    """
    return {
        "action": "edit_interaction",
        "message": message,
    }


@tool
def summarize_interaction(message: str):
    """
    Generate a concise summary.
    """
    return {
        "action": "summarize_interaction",
        "message": message,
    }


@tool
def suggest_followup(message: str):
    """
    Suggest next follow-up actions.
    """
    return {
        "action": "suggest_followup",
        "message": message,
    }


@tool
def meeting_insights(message: str):
    """
    Generate meeting insights.
    """
    return {
        "action": "meeting_insights",
        "message": message,
    }


TOOLS = [
    log_interaction,
    edit_interaction,
    summarize_interaction,
    suggest_followup,
    meeting_insights,
]