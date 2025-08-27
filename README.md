# Tarot Card REST API
Built on FastAPI, SqlAlchemy, and SQLite

# Endpoints
## Tarot
`GET /tarots` - List all tarot cards \
`GET /tarots/{tarot_id}` - Get specific tarot card \
`GET /tarots/{tarot_id}/fortunes` - Get specific tarot card's fortunes \
`GET /tarots/{tarot_id}/keywords` - Get specific tarot card's keywords \
`GET /tarots/{tarot_id}/meanings` - Get all of specific tarot card's meanings \
`GET /tarots/{tarot_id}/meanings/light` - Get specific tarot card's light meanings \
`GET /tarots/{tarot_id}/meanings/shadow` - Get specific tarot card's shadow meanings \

## Arcana
`GET /arcanas` - List all arcanas and related tarots \
`GET /arcanas/{arcana_id}` - Get specific arcana and related tarots \

## Suit
`GET /suits` - List all suits and related tarots \
`GET /suits/{suits_id}` - Get specific suit and related tarots \

