favorites_schema = {
               "$schema": "http://json-schema.org/draft-04/schema#",
               "type": "array",
               "items": {
                              "type": "object",
                              "properties": {
                                             "_cls": {
                                                            "type": "string"
                                             },
                                             "_id": {
                                                            "type": "string"
                                             },
                                             "age_rating": {
                                                            "type": "integer"
                                             },
                                             "alias": {
                                                            "type": "string"
                                             },
                                             "background": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "string"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "string"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "background_1": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "null"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "null"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "background_2": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "null"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "null"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "background_3": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "null"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "null"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "badges": {
                                                            "type": "array",
                                                            "items": {
                                                                           "type": "object",
                                                                           "properties": {
                                                                                          "alias": {
                                                                                                         "type": "string"
                                                                                          },
                                                                                          "background_color": {
                                                                                                         "type": "string",
                                                                                                         "enum": [
                                                                                                                        ""
                                                                                                         ]
                                                                                          },
                                                                                          "background_color_right": {
                                                                                                         "type": "string",
                                                                                                         "enum": [
                                                                                                                        ""
                                                                                                         ]
                                                                                          },
                                                                                          "id": {
                                                                                                         "type": "string"
                                                                                          },
                                                                                          "image_1x": {
                                                                                                         "type": "string"
                                                                                          },
                                                                                          "name": {
                                                                                                         "type": "string"
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
                                                                                                                        ""
                                                                                                         ]
                                                                                          },
                                                                                          "text_color": {
                                                                                                         "type": "string",
                                                                                                         "enum": [
                                                                                                                        ""
                                                                                                         ]
                                                                                          },
                                                                                          "text_color_right": {
                                                                                                         "type": "string",
                                                                                                         "enum": [
                                                                                                                        ""
                                                                                                         ]
                                                                                          },
                                                                                          "text_right": {
                                                                                                         "type": "string",
                                                                                                         "enum": [
                                                                                                                        ""
                                                                                                         ]
                                                                                          },
                                                                                          "type": {
                                                                                                         "type": "string",
                                                                                                         "enum": [
                                                                                                                        "start"
                                                                                                         ]
                                                                                          },
                                                                                          "under_logo_position": {
                                                                                                         "type": "boolean"
                                                                                          }
                                                                           },
                                                                           "additionalProperties": False,
                                                                           "required": [
                                                                                          "alias",
                                                                                          "background_color",
                                                                                          "background_color_right",
                                                                                          "id",
                                                                                          "image_1x",
                                                                                          "name",
                                                                                          "size",
                                                                                          "structure",
                                                                                          "text",
                                                                                          "text_color",
                                                                                          "text_color_right",
                                                                                          "text_right",
                                                                                          "type",
                                                                                          "under_logo_position"
                                                                           ]
                                                            }
                                             },
                                             "banner": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "null"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "null"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "budget": {
                                                            "type": [
                                                                           "null",
                                                                           "string"
                                                            ]
                                             },
                                             "calendar_image": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "null"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "null"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "description": {
                                                            "type": "string"
                                             },
                                             "display": {
                                                            "type": "boolean"
                                             },
                                             "download_options": {
                                                            "type": "string"
                                             },
                                             "downloadable": {
                                                            "type": "boolean"
                                             },
                                             "drm_encrypted": {
                                                            "type": "boolean"
                                             },
                                             "duration": {
                                                            "type": [
                                                                           "null",
                                                                           "integer"
                                                            ]
                                             },
                                             "enabled_for_partner": {
                                                            "type": "boolean"
                                             },
                                             "for_kids": {
                                                            "type": "boolean"
                                             },
                                             "genres": {
                                                            "type": "array",
                                                            "items": {
                                                                           "type": "object",
                                                                           "properties": {
                                                                                          "slug": {
                                                                                                         "type": "string"
                                                                                          },
                                                                                          "title": {
                                                                                                         "type": "string"
                                                                                          },
                                                                                          "url": {
                                                                                                         "type": "string"
                                                                                          }
                                                                           },
                                                                           "additionalProperties": False,
                                                                           "required": [
                                                                                          "slug",
                                                                                          "title",
                                                                                          "url"
                                                                           ]
                                                            }
                                             },
                                             "horizontal": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "string"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "string"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "horizontal_poster": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "string"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "string"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "hot_content": {
                                                            "type": "boolean"
                                             },
                                             "in_subscription": {
                                                            "type": "boolean"
                                             },
                                             "is_disabled": {
                                                            "type": "boolean"
                                             },
                                             "is_free": {
                                                            "type": "boolean"
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
                                             "is_top250": {
                                                            "type": "boolean"
                                             },
                                             "kinopoisk_id": {
                                                            "type": "string"
                                             },
                                             "logotype": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "string"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "null"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "packshot": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "string"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "null"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "play_last_season": {
                                                            "type": "boolean"
                                             },
                                             "playback_options": {
                                                            "type": "string"
                                             },
                                             "premium": {
                                                            "type": "boolean"
                                             },
                                             "quote": {
                                                            "type": "string"
                                             },
                                             "quote_source": {
                                                            "type": "string",
                                                            "enum": [
                                                                           ""
                                                            ]
                                             },
                                             "rating_age": {
                                                            "type": "string"
                                             },
                                             "rating_imdb": {
                                                            "type": "number"
                                             },
                                             "rating_kp": {
                                                            "type": "number"
                                             },
                                             "rating_start": {
                                                            "type": [
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
                                             "special": {
                                                            "type": "boolean"
                                             },
                                             "standard": {
                                                            "type": "boolean"
                                             },
                                             "subtitle": {
                                                            "type": "string",
                                                            "enum": [
                                                                           ""
                                                            ]
                                             },
                                             "thumbnail": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": [
                                                                                                         "null",
                                                                                                         "string"
                                                                                          ]
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "null"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "title": {
                                                            "type": "string"
                                             },
                                             "title_original": {
                                                            "type": "string",
                                                            "enum": [
                                                                           ""
                                                            ]
                                             },
                                             "trailer_src": {
                                                            "type": "string"
                                             },
                                             "uid": {
                                                            "type": "string"
                                             },
                                             "url": {
                                                            "type": "string"
                                             },
                                             "vertical": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "string"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "null"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "vertical_poster": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "image_15x": {
                                                                                          "type": "string"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "string"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "image_15x",
                                                                           "image_1x"
                                                            ]
                                             },
                                             "video_cover": {
                                                            "type": "string"
                                             },
                                             "video_src": {
                                                            "type": "string"
                                             },
                                             "web_url": {
                                                            "type": "string"
                                             },
                                             "year": {
                                                            "type": "integer"
                                             }
                              },
                              "additionalProperties": False,
                              "required": [
                                             "_cls",
                                             "_id",
                                             "age_rating",
                                             "alias",
                                             "background",
                                             "background_1",
                                             "background_2",
                                             "background_3",
                                             "badges",
                                             "banner",
                                             "budget",
                                             "calendar_image",
                                             "description",
                                             "display",
                                             "download_options",
                                             "downloadable",
                                             "drm_encrypted",
                                             "duration",
                                             "enabled_for_partner",
                                             "for_kids",
                                             "genres",
                                             "horizontal",
                                             "horizontal_poster",
                                             "hot_content",
                                             "in_subscription",
                                             "is_disabled",
                                             "is_free",
                                             "is_maxmind_proxy_enabled",
                                             "is_premier",
                                             "is_preview",
                                             "is_top250",
                                             "kinopoisk_id",
                                             "logotype",
                                             "packshot",
                                             "play_last_season",
                                             "playback_options",
                                             "premium",
                                             "quote",
                                             "quote_source",
                                             "rating_age",
                                             "rating_imdb",
                                             "rating_kp",
                                             "rating_start",
                                             "release_date",
                                             "slug",
                                             "special",
                                             "standard",
                                             "subtitle",
                                             "thumbnail",
                                             "title",
                                             "title_original",
                                             "trailer_src",
                                             "uid",
                                             "url",
                                             "vertical",
                                             "vertical_poster",
                                             "video_cover",
                                             "video_src",
                                             "web_url",
                                             "year"
                              ]
               }
}