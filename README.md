# conscious

Helps a large group of people figure out what they think about a topic.

## Development

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then:

* Create the database + schema: `python manage.py migrate`
* Create admin user: `python manage.py createsuperuser`
* Add conversations and statements: [http://127.0.0.1:8000/admin/main/conversation/](http://127.0.0.1:8000/admin/main/conversation/)

See [http://127.0.0.1:8000/] and [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/).

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

## Deployment

We are using ansible to provision machines.

```sh
# install ansible
cd ansible/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# customise configuration
cp .envrc.example .envrc
vim .envrc

# load env variables
source .envrc

# test host is accesible
ansible all -m ping
ansible-inventory --list

# run playbook
ansible-playbook playbook.yaml --verbose

# run playbook on new commits
ansible-playbook -v playbook.yaml --start-at-task="clone"
```

## License

MIT
