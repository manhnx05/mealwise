{
  "name": "MealPlan",
  "type": "object",
  "properties": {
    "week_start": {
      "type": "string",
      "format": "date",
      "description": "Ng\u00e0y b\u1eaft \u0111\u1ea7u tu\u1ea7n"
    },
    "meals": {
      "type": "array",
      "description": "Th\u1ef1c \u0111\u01a1n 7 ng\u00e0y",
      "items": {
        "type": "object",
        "properties": {
          "day": {
            "type": "string"
          },
          "breakfast": {
            "type": "string"
          },
          "lunch": {
            "type": "string"
          },
          "dinner": {
            "type": "string"
          }
        }
      }
    },
    "total_cost": {
      "type": "number",
      "description": "T\u1ed5ng chi ph\u00ed tu\u1ea7n"
    },
    "shopping_list": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "amount": {
            "type": "string"
          },
          "checked": {
            "type": "boolean"
          }
        }
      }
    }
  },
  "required": [
    "week_start"
  ]
}