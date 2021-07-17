# REST api docs

The backend provides a restful api for the minecraft server plugin to consume, as well as for any other web services built around the project.
Any write-operations to the api obviously require authentication.

The url for the api is `<base>/api`.

## Resources

### `GET /shops`
Response body
```
[
  {
    id: Int,
    name: String,
    description: String,
    creation_date: d/m/YYYY HH:MM:SS,
    owners: [
      {
        id: Int,
        name: String
      }, ...
    ]
  }, ...
]
```
### `POST /shops`
Request body
```
{
  shop: String,
  player: String,
  description: String
}
```
Response body
```
[
  {
    id: Int,
    name: String,
    description: String,
    creation_date: d/m/YYYY HH:MM:SS,
    owners: [
      {
        id: Int,
        name: String
      }
    ]
  }
]
```
### `GET /shops/<id>`
Response body
```
[
  {
    id: Int,
    name: String,
    description: String,
    creation_date: d/m/YYYY HH:MM:SS,
    owners: [
      {
        id: Int,
        name: String
      }, ...
    ]
  }
]
```
### `GET /transactions`
Response body
```
[
  {
    shop: String,
    player: String,
    item: String,
    amount: Int,
    timeStamp: ISO
  }, ...
]
```
### `POST /transactions`
Request body
```
[
  {
    shop: String,
    player: String,
    item: String,
    amount: Int,
    timeStamp: ISO
  }, ...
]
```
Response body
```
{
  shop: String,
  player: String,
  item: String,
  amount: Int,
  timeStamp: ISO
}
```
