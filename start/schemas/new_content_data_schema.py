new_content = {
               "$schema": "http://json-schema.org/draft-04/schema#",
               "type": "object",
               "properties": {
                              "alias": {
                                             "type": "string"
                              },
                              "title": {
                                             "type": "string"
                              },
                              "long_description": {
                                             "type": "string"
                              },
                              "short_description": {
                                             "type": "string"
                              },
                              "items": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "id": {
                                                                                          "type": "string"
                                                                           },
                                                                           "cls": {
                                                                                          "type": "string",
                                                                                          "enum": [
                                                                                                         "Series",
                                                                                                         "Movie"
                                                                                          ]
                                                                           },
                                                                           "alias": {
                                                                                          "type": "string"
                                                                           },
                                                                           "background": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "string"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": "string"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "background_1": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": "null"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "background_2": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": "null"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "background_3": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": "null"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "badges": {
                                                                                          "type": "array",
                                                                                          "items": {
                                                                                                         "type": "object",
                                                                                                         "properties": {
                                                                                                                        "id": {
                                                                                                                                       "type": "string"
                                                                                                                        },
                                                                                                                        "alias": {
                                                                                                                                       "type": "string"
                                                                                                                        },
                                                                                                                        "background_color": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "#FF2800",
                                                                                                                                                      "#F2F2F2",
                                                                                                                                                      ""
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "background_color_right": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      ""
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "image_1x": {
                                                                                                                                       "type": [
                                                                                                                                                      "null",
                                                                                                                                                      "string"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "name": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "все серии под постером",
                                                                                                                                                      "все серии под лого",
                                                                                                                                                      "start-фильм под лого",
                                                                                                                                                      "премьера под постером",
                                                                                                                                                      "премьера под лого",
                                                                                                                                                      "новые серии под постером",
                                                                                                                                                      "премьера под лого красный",
                                                                                                                                                      "новые серии под лого",
                                                                                                                                                      "кинопоиск над лого",
                                                                                                                                                      "эксклюзив под лого",
                                                                                                                                                      "иви дно над лого",
                                                                                                                                                      "кино на майские под лого",
                                                                                                                                                      "start-сериал под лого"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "size": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "medium"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "structure": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "single"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "text": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "ВСЕ СЕРИИ",
                                                                                                                                                      "",
                                                                                                                                                      "ПРЕМЬЕРА",
                                                                                                                                                      "НОВЫЕ СЕРИИ",
                                                                                                                                                      "ЭКСКЛЮЗИВ",
                                                                                                                                                      "КИНО НА МАЙСКИЕ"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "text_right": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      ""
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "text_color": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "#FFFFFF",
                                                                                                                                                      "#FF2800",
                                                                                                                                                      ""
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "text_color_right": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      ""
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "type": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "badge",
                                                                                                                                                      "start",
                                                                                                                                                      "logo"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "under_logo_position": {
                                                                                                                                       "type": "boolean"
                                                                                                                        }
                                                                                                         },
                                                                                                         "additionalProperties": False,
                                                                                                         "required": [
                                                                                                                        "id",
                                                                                                                        "alias",
                                                                                                                        "background_color",
                                                                                                                        "background_color_right",
                                                                                                                        "image_1x",
                                                                                                                        "name",
                                                                                                                        "size",
                                                                                                                        "structure",
                                                                                                                        "text",
                                                                                                                        "text_right",
                                                                                                                        "text_color",
                                                                                                                        "text_color_right",
                                                                                                                        "type",
                                                                                                                        "under_logo_position"
                                                                                                         ]
                                                                                          }
                                                                           },
                                                                           "banner": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": "null"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "origin_countries": {
                                                                                          "type": "array",
                                                                                          "items": {
                                                                                                         "type": "object",
                                                                                                         "properties": {
                                                                                                                        "code": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "RU",
                                                                                                                                                      "US",
                                                                                                                                                      "TR"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "title": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "Россия",
                                                                                                                                                      "США",
                                                                                                                                                      "Турция"
                                                                                                                                       ]
                                                                                                                        }
                                                                                                         },
                                                                                                         "additionalProperties": False,
                                                                                                         "required": [
                                                                                                                        "code",
                                                                                                                        "title"
                                                                                                         ]
                                                                                          }
                                                                           },
                                                                           "description": {
                                                                                          "type": "string"
                                                                           },
                                                                           "display": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "downloadable": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "drm_encrypted": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "duration": {
                                                                                          "type": "integer",
                                                                                          "enum": [
                                                                                                         0,
                                                                                                         3419960,
                                                                                                         1521960,
                                                                                                         5845042,
                                                                                                         1856480,
                                                                                                         2135360,
                                                                                                         6840333,
                                                                                                         5494080,
                                                                                                         6464000,
                                                                                                         6857920,
                                                                                                         856040,
                                                                                                         6771042
                                                                                          ]
                                                                           },
                                                                           "for_kids": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "genres": {
                                                                                          "type": "array",
                                                                                          "items": {
                                                                                                         "type": "object",
                                                                                                         "properties": {
                                                                                                                        "title": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "Комедия",
                                                                                                                                                      "Семейный",
                                                                                                                                                      "Детектив",
                                                                                                                                                      "Документальный",
                                                                                                                                                      "Спорт",
                                                                                                                                                      "Драма"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "url": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "/web/genres/comedy",
                                                                                                                                                      "/web/genres/family",
                                                                                                                                                      "/web/genres/detective",
                                                                                                                                                      "/web/genres/documental",
                                                                                                                                                      "/web/genres/sport",
                                                                                                                                                      "/web/genres/drama"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "slug": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "/genres/comedy",
                                                                                                                                                      "/genres/family",
                                                                                                                                                      "/genres/detective",
                                                                                                                                                      "/genres/documental",
                                                                                                                                                      "/genres/sport",
                                                                                                                                                      "/genres/drama"
                                                                                                                                       ]
                                                                                                                        }
                                                                                                         },
                                                                                                         "additionalProperties": False,
                                                                                                         "required": [
                                                                                                                        "title",
                                                                                                                        "url",
                                                                                                                        "slug"
                                                                                                         ]
                                                                                          }
                                                                           },
                                                                           "horizontal": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "string"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": "string"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "is_maxmind_proxy_enabled": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "is_premier": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "is_preview": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "items_total": {
                                                                                          "type": "integer",
                                                                                          "enum": [
                                                                                                         1,
                                                                                                         0,
                                                                                                         2,
                                                                                                         3,
                                                                                                         4
                                                                                          ]
                                                                           },
                                                                           "logotype": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": "string"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "packshot": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": "string"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "playback_options": {
                                                                                          "type": "string"
                                                                           },
                                                                           "publish": {
                                                                                          "type": "string"
                                                                           },
                                                                           "rating_age": {
                                                                                          "type": "string",
                                                                                          "enum": [
                                                                                                         "18+",
                                                                                                         "16+",
                                                                                                         "12+",
                                                                                                         "6+"
                                                                                          ]
                                                                           },
                                                                           "rating_start": {
                                                                                          "type": [
                                                                                                         "null",
                                                                                                         "number",
                                                                                                         "integer"
                                                                                          ]
                                                                           },
                                                                           "release_date": {
                                                                                          "type": "integer"
                                                                           },
                                                                           "slug": {
                                                                                          "type": "string"
                                                                           },
                                                                           "start_release_date": {
                                                                                          "type": "string"
                                                                           },
                                                                           "tags": {
                                                                                          "type": "array",
                                                                                          "items": {
                                                                                                         "type": "string",
                                                                                                         "enum": [
                                                                                                                        "BIPromoProduct",
                                                                                                                        "Exclusive",
                                                                                                                        "Originals",
                                                                                                                        "Lg",
                                                                                                                        "SimilarsInManualControl",
                                                                                                                        "Топ 30",
                                                                                                                        "4K",
                                                                                                                        "AutoBumper"
                                                                                                         ]
                                                                                          }
                                                                           },
                                                                           "thumbnail": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": [
                                                                                                                                       "null",
                                                                                                                                       "string"
                                                                                                                        ]
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "title": {
                                                                                          "type": "string"
                                                                           },
                                                                           "trailer_src": {
                                                                                          "type": "string"
                                                                           },
                                                                           "url": {
                                                                                          "type": "string"
                                                                           },
                                                                           "vertical": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "image_1x": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "image_15x": {
                                                                                                                        "type": "string"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "image_1x",
                                                                                                         "image_15x"
                                                                                          ]
                                                                           },
                                                                           "web_url": {
                                                                                          "type": "string"
                                                                           },
                                                                           "year": {
                                                                                          "type": "integer",
                                                                                          "enum": [
                                                                                                         2024
                                                                                          ]
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "id",
                                                                           "cls",
                                                                           "alias",
                                                                           "background",
                                                                           "background_1",
                                                                           "background_2",
                                                                           "background_3",
                                                                           "badges",
                                                                           "banner",
                                                                           "origin_countries",
                                                                           "description",
                                                                           "display",
                                                                           "downloadable",
                                                                           "drm_encrypted",
                                                                           "duration",
                                                                           "for_kids",
                                                                           "genres",
                                                                           "horizontal",
                                                                           "is_maxmind_proxy_enabled",
                                                                           "is_premier",
                                                                           "is_preview",
                                                                           "items_total",
                                                                           "logotype",
                                                                           "packshot",
                                                                           "playback_options",
                                                                           "publish",
                                                                           "rating_age",
                                                                           "rating_start",
                                                                           "release_date",
                                                                           "slug",
                                                                           "start_release_date",
                                                                           "tags",
                                                                           "thumbnail",
                                                                           "title",
                                                                           "trailer_src",
                                                                           "url",
                                                                           "vertical",
                                                                           "web_url",
                                                                           "year"
                                                            ]
                                             }
                              },
                              "items_total": {
                                             "type": "integer"
                              }
               },
               "additionalProperties": False,
               "required": [
                              "alias",
                              "title",
                              "long_description",
                              "short_description",
                              "items",
                              "items_total"
               ]
}