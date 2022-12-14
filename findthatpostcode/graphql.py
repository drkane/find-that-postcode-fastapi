from typing import List, Optional

import strawberry
from graphql.pyutils import camel_to_snake
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info

from findthatpostcode import crud, schemas
from findthatpostcode.db import get_db


def get_selected_fields(info):
    for s in info.selected_fields[0].selections:
        yield camel_to_snake(s.name)


@strawberry.type
class Query:
    @strawberry.field
    def get_postcode(self, postcode: str, info: Info) -> Optional[schemas.Postcode]:
        db = get_db()
        return crud.get_postcode(db, postcode, fields=get_selected_fields(info))

    @strawberry.field
    def get_postcodes(
        self, postcodes: List[str], info: Info
    ) -> Optional[List[schemas.Postcode]]:
        db = get_db()
        return crud.get_postcodes(db, postcodes, fields=get_selected_fields(info))

    @strawberry.field
    def get_nearest_point(
        self, lat: float, long: float, info: Info
    ) -> Optional[schemas.NearestPoint]:
        db = get_db()
        return crud.get_nearest_postcode(
            db, lat, long, fields=get_selected_fields(info)
        )

    @strawberry.field
    def get_hashes(self, hashes: List[str], info: Info) -> List[schemas.Postcode]:
        db = get_db()
        postcode_items = list(
            crud.get_postcode_by_hash(db, hashes, fields=get_selected_fields(info))
        )
        return postcode_items

    @strawberry.field
    def get_area(self, areacode: str, info: Info) -> Optional[schemas.Area]:
        db = get_db()
        return crud.get_area(db, areacode, fields=get_selected_fields(info))


schema = strawberry.Schema(Query)

router = GraphQLRouter(schema)
