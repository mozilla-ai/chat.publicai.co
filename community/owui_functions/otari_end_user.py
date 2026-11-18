"""
title: Otari end user
description: Names the signed-in Open WebUI user as the Otari end user of each request.
version: 0.1.0

Otari bills, budgets and rate-limits each chat user as an end user of Open WebUI's one service
key, and takes the end user from the request's `user` field. Open WebUI sends the user only in
X-OpenWebUI-User-* headers (what LiteLLM's custom_auth.py reads today), so this filter copies the
user's id into the body. Enable it as a global filter.
"""

from typing import Optional

from pydantic import BaseModel


class Filter:
    class Valves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()

    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        if __user__ and __user__.get("id"):
            body["user"] = __user__["id"]
        return body
