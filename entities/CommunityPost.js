{
  "name": "CommunityPost",
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "description": "T\u00ean m\u00f3n \u0103n chia s\u1ebb"
    },
    "description": {
      "type": "string",
      "description": "M\u00f4 t\u1ea3"
    },
    "image_url": {
      "type": "string",
      "description": "\u1ea2nh m\u00f3n \u0103n"
    },
    "recipe_text": {
      "type": "string",
      "description": "C\u00f4ng th\u1ee9c n\u1ea5u"
    },
    "rating": {
      "type": "number",
      "description": "\u0110\u00e1nh gi\u00e1 trung b\u00ecnh"
    },
    "rating_count": {
      "type": "number",
      "description": "S\u1ed1 l\u01b0\u1ee3t \u0111\u00e1nh gi\u00e1"
    },
    "author_name": {
      "type": "string"
    },
    "comments": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "author": {
            "type": "string"
          },
          "text": {
            "type": "string"
          },
          "date": {
            "type": "string"
          }
        }
      }
    }
  },
  "required": [
    "title"
  ]
}