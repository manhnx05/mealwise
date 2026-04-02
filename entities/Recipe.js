{
  "name": "Recipe",
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "description": "T\u00ean m\u00f3n \u0103n"
    },
    "description": {
      "type": "string",
      "description": "M\u00f4 t\u1ea3 ng\u1eafn v\u1ec1 m\u00f3n \u0103n"
    },
    "image_url": {
      "type": "string",
      "description": "URL h\u00ecnh \u1ea3nh m\u00f3n \u0103n"
    },
    "video_url": {
      "type": "string",
      "description": "URL video h\u01b0\u1edbng d\u1eabn"
    },
    "cook_time": {
      "type": "number",
      "description": "Th\u1eddi gian n\u1ea5u (ph\u00fat)"
    },
    "servings": {
      "type": "number",
      "description": "S\u1ed1 ng\u01b0\u1eddi \u0103n"
    },
    "cost": {
      "type": "number",
      "description": "Chi ph\u00ed \u01b0\u1edbc t\u00ednh (VN\u0110)"
    },
    "calories": {
      "type": "number",
      "description": "T\u1ed5ng calo (kcal)"
    },
    "protein": {
      "type": "number",
      "description": "Protein (g)"
    },
    "fat": {
      "type": "number",
      "description": "Ch\u1ea5t b\u00e9o (g)"
    },
    "fiber": {
      "type": "number",
      "description": "Ch\u1ea5t x\u01a1 (g)"
    },
    "carbs": {
      "type": "number",
      "description": "Carbs (g)"
    },
    "category": {
      "type": "string",
      "enum": [
        "quick_meal",
        "low_fat",
        "weight_loss",
        "gym",
        "healthy",
        "budget",
        "vegetarian"
      ],
      "description": "Ph\u00e2n lo\u1ea1i m\u00f3n \u0103n"
    },
    "ingredients": {
      "type": "array",
      "description": "Danh s\u00e1ch nguy\u00ean li\u1ec7u",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "amount": {
            "type": "string"
          },
          "calories": {
            "type": "number"
          },
          "cost": {
            "type": "number"
          }
        }
      }
    },
    "steps": {
      "type": "array",
      "description": "C\u00e1c b\u01b0\u1edbc n\u1ea5u",
      "items": {
        "type": "object",
        "properties": {
          "step_number": {
            "type": "number"
          },
          "instruction": {
            "type": "string"
          },
          "image_url": {
            "type": "string"
          }
        }
      }
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Tags cho t\u00ecm ki\u1ebfm"
    }
  },
  "required": [
    "title",
    "cook_time"
  ]
}