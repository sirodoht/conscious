# conscious

Helps a large group of people figure out what they think about a topic.

## Development

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## API

POST `api/conversations/<conversation_id>/votes/active/`

Request body:

```
{
    "user_id": int,
    "vote": str:<agree|disagree|pass>,
}
```

Headers:

```
Authorization: Bearer <api_key>
```

## License

MIT
