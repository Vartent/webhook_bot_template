# webhook_bot_template

## FastAPI, Aiogram, SQLAlchemy, Alembic

**Installation:**   
`pip install -r requirements.txt`

Into **.env** add:
1. **Bot token** (*ask [@BotFather](https://t.me/BotFather)*);
2. **DataBase link** (*configure database an get link to it*);
3. **Public IP adrees** (*[Ngrok](https://ngrok.com/download) for dev, [Nginx](https://nginx.org/) for prod*)

To run migration:   
`alembic revision --autogenerate -m "create user table"`

To apply generated migration:   
`alembic upgrade head`
