# Open WebUI on Otari (prototype)

A prototype replaces Zuplo and LiteLLM with [Otari](https://github.com/mozilla-ai/otari). It lives
in the `otari/` directory of the `otari-prototype` branch of
[mozilla-ai/platform.publicai.co](https://github.com/mozilla-ai/platform.publicai.co/tree/otari-prototype/otari),
which has the compose stack, the Lago wallet overlay and a smoke test.

For chat, two things change:

- **Connection.** Open WebUI's OpenAI connection points at Otari (`OPENAI_API_BASE_URL=<otari>/api/v1`)
  with one Otari service key, in place of the LiteLLM master key.
- **Chat users.** LiteLLM's `custom_auth.py` reads the `X-OpenWebUI-User-Id` header and gives each
  user the `public_ai_free` budget. Otari takes the end user from the request's `user` field, so
  install [`community/owui_functions/otari_end_user.py`](../../community/owui_functions/otari_end_user.py)
  as a global filter. Each chat user then becomes an end user of the service key, on the budget the
  key starts end users on, with their own spend and rate limit.

`charts/platform/charts/otari` deploys Otari with the overlay. It is off by default
(`otari.enabled: false` in `charts/platform/values.yaml`) and runs beside LiteLLM, which stays on.
Its `values.yaml` lists Public AI's model hosts as Otari hosted providers and the secrets to add
before turning it on. The image it names is built from `otari/Dockerfile` in the platform repo
and is not published yet.
