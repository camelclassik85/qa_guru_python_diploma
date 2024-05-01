series_schema = {
               "$schema": "http://json-schema.org/draft-04/schema#",
               "type": "object",
               "properties": {
                              "_cls": {
                                             "type": "string"
                              },
                              "_id": {
                                             "type": "string"
                              },
                              "additional_content": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "announcement": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "description": {
                                                                                          "type": "string"
                                                                           },
                                                                           "packshot": {
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
                                                                           "restrictions": {
                                                                                          "type": "array",
                                                                                          "items": {
                                                                                                         "items": {},
                                                                                                         "additionalProperties": False
                                                                                          }
                                                                           },
                                                                           "title": {
                                                                                          "type": "string"
                                                                           },
                                                                           "start_id": {
                                                                                          "type": "integer"
                                                                           },
                                                                           "uid": {
                                                                                          "type": "string"
                                                                           },
                                                                           "video_src": {
                                                                                          "type": "string"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "announcement",
                                                                           "description",
                                                                           "packshot",
                                                                           "restrictions",
                                                                           "title",
                                                                           "start_id",
                                                                           "uid",
                                                                           "video_src"
                                                            ]
                                             }
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
                                                                                          "type": "string"
                                                                           },
                                                                           "background_color_right": {
                                                                                          "type": "string"
                                                                           },
                                                                           "image_1x": {
                                                                                          "type": "string"
                                                                           },
                                                                           "name": {
                                                                                          "type": "string"
                                                                           },
                                                                           "size": {
                                                                                          "type": "string"
                                                                           },
                                                                           "structure": {
                                                                                          "type": "string"
                                                                           },
                                                                           "text": {
                                                                                          "type": "string"
                                                                           },
                                                                           "text_right": {
                                                                                          "type": "string"
                                                                           },
                                                                           "text_color": {
                                                                                          "type": "string"
                                                                           },
                                                                           "text_color_right": {
                                                                                          "type": "string"
                                                                           },
                                                                           "type": {
                                                                                          "type": "string"
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
                              "budget": {
                                             "type": "null"
                              },
                              "cast": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "alias": {
                                                                                          "type": "string"
                                                                           },
                                                                           "character": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "biography": {
                                                                                                                        "type": "string",
                                                                                                                        "enum": [
                                                                                                                                       ""
                                                                                                                        ]
                                                                                                         },
                                                                                                         "main_character": {
                                                                                                                        "type": "boolean"
                                                                                                         },
                                                                                                         "name": {
                                                                                                                        "type": "string"
                                                                                                         },
                                                                                                         "photo": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "photo_app_section": {
                                                                                                                        "type": [
                                                                                                                                       "string",
                                                                                                                                       "null"
                                                                                                                        ]
                                                                                                         },
                                                                                                         "start_id": {
                                                                                                                        "type": "integer"
                                                                                                         },
                                                                                                         "weight": {
                                                                                                                        "type": [
                                                                                                                                       "integer",
                                                                                                                                       "null"
                                                                                                                        ]
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "biography",
                                                                                                         "main_character",
                                                                                                         "name",
                                                                                                         "photo",
                                                                                                         "photo_app_section",
                                                                                                         "start_id",
                                                                                                         "weight"
                                                                                          ]
                                                                           },
                                                                           "filmography": {
                                                                                          "type": "string"
                                                                           },
                                                                           "name": {
                                                                                          "type": "string"
                                                                           },
                                                                           "photo": {
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
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "alias",
                                                                           "character",
                                                                           "filmography",
                                                                           "name",
                                                                           "photo"
                                                            ]
                                             }
                              },
                              "color": {
                                             "type": "object",
                                             "properties": {
                                                            "back_color_1": {
                                                                           "type": "string"
                                                            },
                                                            "back_color_2": {
                                                                           "type": "string"
                                                            },
                                                            "font_color": {
                                                                           "type": "string"
                                                            }
                                             },
                                             "additionalProperties": False,
                                             "required": [
                                                            "back_color_1",
                                                            "back_color_2",
                                                            "font_color"
                                             ]
                              },
                              "composers": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "alias": {
                                                                                          "type": "string"
                                                                           },
                                                                           "character": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "photo": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "photo_app_section": {
                                                                                                                        "type": "null"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "photo",
                                                                                                         "photo_app_section"
                                                                                          ]
                                                                           },
                                                                           "filmography": {
                                                                                          "type": "string"
                                                                           },
                                                                           "name": {
                                                                                          "type": "string"
                                                                           },
                                                                           "photo": {
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
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "alias",
                                                                           "character",
                                                                           "filmography",
                                                                           "name",
                                                                           "photo"
                                                            ]
                                             }
                              },
                              "description": {
                                             "type": "string"
                              },
                              "directors": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "alias": {
                                                                                          "type": "string"
                                                                           },
                                                                           "character": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "photo": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "photo_app_section": {
                                                                                                                        "type": "null"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "photo",
                                                                                                         "photo_app_section"
                                                                                          ]
                                                                           },
                                                                           "filmography": {
                                                                                          "type": "string"
                                                                           },
                                                                           "name": {
                                                                                          "type": "string"
                                                                           },
                                                                           "photo": {
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
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "alias",
                                                                           "character",
                                                                           "filmography",
                                                                           "name",
                                                                           "photo"
                                                            ]
                                             }
                              },
                              "display": {
                                             "type": "boolean"
                              },
                              "downloadable": {
                                             "type": "boolean"
                              },
                              "enabled_for_partner": {
                                             "type": "boolean"
                              },
                              "facts": {
                                             "type": "array",
                                             "items": {
                                                            "type": "string"
                                             }
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
                              "hashtags": {
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
                                                                           "title": {
                                                                                          "type": "string"
                                                                           },
                                                                           "text_color": {
                                                                                          "type": "string",
                                                                                          "enum": [
                                                                                                         "#FF987D",
                                                                                                         "#00E4BB",
                                                                                                         "#FFF900",
                                                                                                         "#00B9F1",
                                                                                                         "#9300FF"
                                                                                          ]
                                                                           },
                                                                           "url": {
                                                                                          "type": "string"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "id",
                                                                           "alias",
                                                                           "title",
                                                                           "text_color",
                                                                           "url"
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
                              "horizontal_poster": {
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
                              "is_premier": {
                                             "type": "boolean"
                              },
                              "is_preview": {
                                             "type": "boolean"
                              },
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
                                                                           "description": {
                                                                                          "type": "string"
                                                                           },
                                                                           "display": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "downloadable": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "enabled_for_partner": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "for_kids": {
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
                                                                           "is_premier": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "is_preview": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "items": {
                                                                                          "type": "array",
                                                                                          "items": {
                                                                                                         "type": "object",
                                                                                                         "properties": {
                                                                                                                        "_cls": {
                                                                                                                                       "type": "string",
                                                                                                                                       "enum": [
                                                                                                                                                      "Episode"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "_id": {
                                                                                                                                       "type": "string"
                                                                                                                        },
                                                                                                                        "announcement": {
                                                                                                                                       "type": "boolean"
                                                                                                                        },
                                                                                                                        "badges": {
                                                                                                                                       "type": "array",
                                                                                                                                       "items": {
                                                                                                                                                      "items": {},
                                                                                                                                                      "additionalProperties": False
                                                                                                                                       }
                                                                                                                        },
                                                                                                                        "description": {
                                                                                                                                       "type": "string"
                                                                                                                        },
                                                                                                                        "display": {
                                                                                                                                       "type": "boolean"
                                                                                                                        },
                                                                                                                        "is_free": {
                                                                                                                                       "type": "boolean"
                                                                                                                        },
                                                                                                                        "duration": {
                                                                                                                                       "type": "integer"
                                                                                                                        },
                                                                                                                        "free_for_authorized": {
                                                                                                                                       "type": "boolean"
                                                                                                                        },
                                                                                                                        "num": {
                                                                                                                                       "type": "integer"
                                                                                                                        },
                                                                                                                        "number": {
                                                                                                                                       "type": "integer"
                                                                                                                        },
                                                                                                                        "packshot": {
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
                                                                                                                        "packshot_free": {
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
                                                                                                                        "playback_options": {
                                                                                                                                       "type": "string"
                                                                                                                        },
                                                                                                                        "start_release_date": {
                                                                                                                                       "type": [
                                                                                                                                                      "string",
                                                                                                                                                      "null"
                                                                                                                                       ]
                                                                                                                        },
                                                                                                                        "release_date": {
                                                                                                                                       "type": "integer"
                                                                                                                        },
                                                                                                                        "restrictions": {
                                                                                                                                       "type": "array",
                                                                                                                                       "items": {
                                                                                                                                                      "items": {},
                                                                                                                                                      "additionalProperties": False
                                                                                                                                       }
                                                                                                                        },
                                                                                                                        "seo_text": {
                                                                                                                                       "type": "string"
                                                                                                                        },
                                                                                                                        "start_id": {
                                                                                                                                       "type": "integer"
                                                                                                                        },
                                                                                                                        "title": {
                                                                                                                                       "type": "string"
                                                                                                                        },
                                                                                                                        "uid": {
                                                                                                                                       "type": "string"
                                                                                                                        },
                                                                                                                        "unavailable_by_geo": {
                                                                                                                                       "type": "boolean"
                                                                                                                        },
                                                                                                                        "url": {
                                                                                                                                       "type": "string"
                                                                                                                        },
                                                                                                                        "web_url": {
                                                                                                                                       "type": "string"
                                                                                                                        }
                                                                                                         },
                                                                                                         "additionalProperties": False,
                                                                                                         "required": [
                                                                                                                        "_cls",
                                                                                                                        "_id",
                                                                                                                        "announcement",
                                                                                                                        "badges",
                                                                                                                        "description",
                                                                                                                        "display",
                                                                                                                        "is_free",
                                                                                                                        "duration",
                                                                                                                        "free_for_authorized",
                                                                                                                        "num",
                                                                                                                        "number",
                                                                                                                        "packshot",
                                                                                                                        "packshot_free",
                                                                                                                        "playback_options",
                                                                                                                        "start_release_date",
                                                                                                                        "release_date",
                                                                                                                        "restrictions",
                                                                                                                        "seo_text",
                                                                                                                        "start_id",
                                                                                                                        "title",
                                                                                                                        "uid",
                                                                                                                        "unavailable_by_geo",
                                                                                                                        "url",
                                                                                                                        "web_url"
                                                                                                         ]
                                                                                          }
                                                                           },
                                                                           "logotype": {
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
                                                                           "num": {
                                                                                          "type": "integer"
                                                                           },
                                                                           "number": {
                                                                                          "type": "integer"
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
                                                                           "play_last_season": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "playback_options": {
                                                                                          "type": "string"
                                                                           },
                                                                           "publish": {
                                                                                          "type": "string"
                                                                           },
                                                                           "rating_age": {
                                                                                          "type": "string"
                                                                           },
                                                                           "release_date": {
                                                                                          "type": "integer"
                                                                           },
                                                                           "restrictions": {
                                                                                          "type": "array",
                                                                                          "items": {
                                                                                                         "items": {},
                                                                                                         "additionalProperties": False
                                                                                          }
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
                                                                           "start_release_date": {
                                                                                          "type": "string"
                                                                           },
                                                                           "subtitle": {
                                                                                          "type": "string"
                                                                           },
                                                                           "thumbnail": {
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
                                                                           "title": {
                                                                                          "type": "string"
                                                                           },
                                                                           "title_original": {
                                                                                          "type": "string"
                                                                           },
                                                                           "uid": {
                                                                                          "type": "string"
                                                                           },
                                                                           "unavailable_by_geo": {
                                                                                          "type": "boolean"
                                                                           },
                                                                           "unpublish": {
                                                                                          "type": "integer"
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
                                                                           "display",
                                                                           "downloadable",
                                                                           "enabled_for_partner",
                                                                           "for_kids",
                                                                           "in_subscription",
                                                                           "is_disabled",
                                                                           "is_free",
                                                                           "is_premier",
                                                                           "is_preview",
                                                                           "items",
                                                                           "logotype",
                                                                           "num",
                                                                           "number",
                                                                           "packshot",
                                                                           "play_last_season",
                                                                           "playback_options",
                                                                           "publish",
                                                                           "rating_age",
                                                                           "release_date",
                                                                           "restrictions",
                                                                           "slug",
                                                                           "special",
                                                                           "standard",
                                                                           "start_release_date",
                                                                           "subtitle",
                                                                           "thumbnail",
                                                                           "title",
                                                                           "title_original",
                                                                           "uid",
                                                                           "unavailable_by_geo",
                                                                           "unpublish",
                                                                           "url",
                                                                           "vertical",
                                                                           "year"
                                                            ]
                                             }
                              },
                              "items_total": {
                                             "type": "integer"
                              },
                              "kinopoisk_id": {
                                             "type": "string"
                              },
                              "locales": {
                                             "type": "array",
                                             "items": {
                                                            "type": "string"
                                             }
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
                              "operators": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "alias": {
                                                                                          "type": "string"
                                                                           },
                                                                           "character": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "photo": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "photo_app_section": {
                                                                                                                        "type": "null"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "photo",
                                                                                                         "photo_app_section"
                                                                                          ]
                                                                           },
                                                                           "filmography": {
                                                                                          "type": "string"
                                                                           },
                                                                           "name": {
                                                                                          "type": "string"
                                                                           },
                                                                           "photo": {
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
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "alias",
                                                                           "character",
                                                                           "filmography",
                                                                           "name",
                                                                           "photo"
                                                            ]
                                             }
                              },
                              "origin_countries": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "code": {
                                                                                          "type": "string"
                                                                           },
                                                                           "title": {
                                                                                          "type": "string"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "code",
                                                                           "title"
                                                            ]
                                             }
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
                              "play_last_season": {
                                             "type": "boolean"
                              },
                              "playback_options": {
                                             "type": "string"
                              },
                              "producers": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "alias": {
                                                                                          "type": "string"
                                                                           },
                                                                           "character": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "photo": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "photo_app_section": {
                                                                                                                        "type": "null"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "photo",
                                                                                                         "photo_app_section"
                                                                                          ]
                                                                           },
                                                                           "filmography": {
                                                                                          "type": "string"
                                                                           },
                                                                           "name": {
                                                                                          "type": "string"
                                                                           },
                                                                           "photo": {
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
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "alias",
                                                                           "character",
                                                                           "filmography",
                                                                           "name",
                                                                           "photo"
                                                            ]
                                             }
                              },
                              "publish": {
                                             "type": "string"
                              },
                              "quote": {
                                             "type": "string"
                              },
                              "quote_source": {
                                             "type": "string"
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
                                             "type": "number"
                              },
                              "release_date": {
                                             "type": "integer"
                              },
                              "release_year_end": {
                                             "type": "null"
                              },
                              "release_year_start": {
                                             "type": "integer"
                              },
                              "restrictions": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "id": {
                                                                                          "type": "string"
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "id"
                                                            ]
                                             }
                              },
                              "seo": {
                                             "type": "object",
                                             "properties": {
                                                            "long_description": {
                                                                           "type": "string"
                                                            },
                                                            "short_description": {
                                                                           "type": "string"
                                                            },
                                                            "subject": {
                                                                           "type": "string"
                                                            }
                                             },
                                             "additionalProperties": False,
                                             "required": [
                                                            "long_description",
                                                            "short_description",
                                                            "subject"
                                             ]
                              },
                              "slug": {
                                             "type": "string"
                              },
                              "similar": {
                                             "type": "string"
                              },
                              "special": {
                                             "type": "boolean"
                              },
                              "special_description": {
                                             "type": "object",
                                             "properties": {
                                                            "paragraph_1": {
                                                                           "type": "string"
                                                            },
                                                            "paragraph_2": {
                                                                           "type": "string"
                                                            },
                                                            "paragraph_3": {
                                                                           "type": "string"
                                                            },
                                                            "paragraph_4": {
                                                                           "type": "string"
                                                            }
                                             },
                                             "additionalProperties": False,
                                             "required": [
                                                            "paragraph_1",
                                                            "paragraph_2",
                                                            "paragraph_3",
                                                            "paragraph_4"
                                             ]
                              },
                              "standard": {
                                             "type": "boolean"
                              },
                              "start_release_date": {
                                             "type": "string"
                              },
                              "subtitle": {
                                             "type": "string"
                              },
                              "thumbnail": {
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
                              "unpublish": {
                                             "type": "integer"
                              },
                              "unavailable_by_geo": {
                                             "type": "boolean"
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
                              "vertical_poster": {
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
                              "web_url": {
                                             "type": "string"
                              },
                              "writers": {
                                             "type": "array",
                                             "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                           "alias": {
                                                                                          "type": "string"
                                                                           },
                                                                           "character": {
                                                                                          "type": "object",
                                                                                          "properties": {
                                                                                                         "photo": {
                                                                                                                        "type": "null"
                                                                                                         },
                                                                                                         "photo_app_section": {
                                                                                                                        "type": "null"
                                                                                                         }
                                                                                          },
                                                                                          "additionalProperties": False,
                                                                                          "required": [
                                                                                                         "photo",
                                                                                                         "photo_app_section"
                                                                                          ]
                                                                           },
                                                                           "filmography": {
                                                                                          "type": "string"
                                                                           },
                                                                           "name": {
                                                                                          "type": "string"
                                                                           },
                                                                           "photo": {
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
                                                                           }
                                                            },
                                                            "additionalProperties": False,
                                                            "required": [
                                                                           "alias",
                                                                           "character",
                                                                           "filmography",
                                                                           "name",
                                                                           "photo"
                                                            ]
                                             }
                              },
                              "year": {
                                             "type": "integer"
                              }
               },
               "additionalProperties": False,
               "required": [
                              "_cls",
                              "_id",
                              "additional_content",
                              "alias",
                              "background",
                              "badges",
                              "banner",
                              "budget",
                              "cast",
                              "color",
                              "composers",
                              "description",
                              "directors",
                              "display",
                              "downloadable",
                              "enabled_for_partner",
                              "facts",
                              "for_kids",
                              "genres",
                              "hashtags",
                              "horizontal",
                              "horizontal_poster",
                              "in_subscription",
                              "is_4k",
                              "is_51",
                              "is_disabled",
                              "is_free",
                              "is_premier",
                              "is_preview",
                              "items",
                              "items_total",
                              "kinopoisk_id",
                              "locales",
                              "logotype",
                              "operators",
                              "origin_countries",
                              "packshot",
                              "play_last_season",
                              "playback_options",
                              "producers",
                              "publish",
                              "quote",
                              "quote_source",
                              "rating_age",
                              "rating_imdb",
                              "rating_kp",
                              "rating_start",
                              "release_date",
                              "release_year_end",
                              "release_year_start",
                              "restrictions",
                              "seo",
                              "slug",
                              "similar",
                              "special",
                              "special_description",
                              "standard",
                              "start_release_date",
                              "subtitle",
                              "thumbnail",
                              "title",
                              "title_original",
                              "trailer_src",
                              "uid",
                              "unpublish",
                              "unavailable_by_geo",
                              "url",
                              "vertical",
                              "vertical_poster",
                              "web_url",
                              "writers",
                              "year"
               ]
}