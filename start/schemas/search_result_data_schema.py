search_result = {
               "$schema": "http://json-schema.org/draft-04/schema#",
               "type": "object",
               "properties": {
                              "items": {
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
                                                                           "badges": {
                                                                                          "type": "array",
                                                                                          "items": {
                                                                                                         "items": {},
                                                                                                         "additionalProperties": False
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
                                                                           "description": {
                                                                                          "type": "string"
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
                                                                                          "type": "integer"
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
                                                                                                                        }
                                                                                                         },
                                                                                                         "additionalProperties": False,
                                                                                                         "required": [
                                                                                                                        "slug",
                                                                                                                        "title"
                                                                                                         ]
                                                                                          }
                                                                           },
                                                                           "genres_string": {
                                                                                          "type": "string"
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
                                                                           "hot_content": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "in_subscription": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "is_4k": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "is_51": {
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
                                                                           "meta": {
                                                                                          "type": "array",
                                                                                          "items": {
                                                                                                         "items": {},
                                                                                                         "additionalProperties": False
                                                                                          }
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
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "source": {
                                                                                                                        "type": "string"
                                                                                                         },
                                                                                                         "text": {
                                                                                                                        "type": "string"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "source",
                                                                                                         "text"
                                                                                          ]
                                                                           },
                                                                           "quote_source": {
                                                                                          "type": "string"
                                                                           },
                                                                           "rating_age": {
                                                                                          "type": "string"
                                                                           },
                                                                           "rating_start": {
                                                                                          "type": "number"
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
                                                                                          "type": "string"
                                                                           },
                                                                           "summary": {
                                                                                          "type": "string"
                                                                           },
                                                                           "thumbnail": {
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
                                                                           "title": {
                                                                                          "type": "string"
                                                                           },
                                                                           "title_original": {
                                                                                          "type": "string"
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
                                                                           "video_cover": {
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
                                                                           "alias",
                                                                           "background",
                                                                           "badges",
                                                                           "banner",
                                                                           "description",
                                                                           "download_options",
                                                                           "downloadable",
                                                                           "drm_encrypted",
                                                                           "duration",
                                                                           "enabled_for_partner",
                                                                           "for_kids",
                                                                           "genres",
                                                                           "genres_string",
                                                                           "horizontal",
                                                                           "hot_content",
                                                                           "in_subscription",
                                                                           "is_4k",
                                                                           "is_51",
                                                                           "is_disabled",
                                                                           "is_free",
                                                                           "is_maxmind_proxy_enabled",
                                                                           "is_premier",
                                                                           "is_preview",
                                                                           "is_top250",
                                                                           "logotype",
                                                                           "meta",
                                                                           "packshot",
                                                                           "play_last_season",
                                                                           "playback_options",
                                                                           "premium",
                                                                           "quote",
                                                                           "quote_source",
                                                                           "rating_age",
                                                                           "rating_start",
                                                                           "release_date",
                                                                           "slug",
                                                                           "special",
                                                                           "standard",
                                                                           "subtitle",
                                                                           "summary",
                                                                           "thumbnail",
                                                                           "title",
                                                                           "title_original",
                                                                           "trailer_src",
                                                                           "uid",
                                                                           "url",
                                                                           "vertical",
                                                                           "video_cover",
                                                                           "web_url",
                                                                           "year"
                                                            ]
                                             }
                              },
                              "meta": {
                                             "type": "object",
                                             "properties": {
                                                            "items_count": {
                                                                           "type": "integer"
                                                            },
                                                            "items_limit": {
                                                                           "type": "integer"
                                                            },
                                                            "items_offset": {
                                                                           "type": "integer"
                                                            }
                                             },
                                             "additionalProperties": False,
                                             "required": [
                                                            "items_count",
                                                            "items_limit",
                                                            "items_offset"
                                             ]
                              },
                              "original_query": {
                                             "type": "string"
                              },
                              "status": {
                                             "type": "string"
                              },
                              "suggestion": {
                                             "type": "null"
                              }
               },
               "additionalProperties": False,
               "required": [
                              "items",
                              "meta",
                              "original_query",
                              "status",
                              "suggestion"
               ]
}