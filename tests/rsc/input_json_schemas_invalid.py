schema_nested_2_invalid_JSON = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {
      "column_name_missing_quotes: {
        "type": [
          "null",
          "integer"
        ]
      } }
  },
  "key_properties": [
    "Id"
  ]
}
"""


invalild_schema_top_field_empty_props = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {

      "Languages": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "string": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": "string"
            }
          }
        }
      },


      "Languages_Empty_Properties": {
        "type": [
          "null",
          "object"
        ],
        "properties": {

        }
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalild_schema_top_field_empty_type = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {

      "Languages": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "string": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": "string"
            }
          }
        }
      },

      "BudgetId_empty_type": {
        "type": [
        ]
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_subfield_empty_props = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {

      "ForwardCompatibilityMap": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      },
      "ForwardCompatibilityMap_subfield_empty_props": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "properties": {
                  }
                }
              }
            }
          }
        }
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_subfield_empty_type = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {

      "ForwardCompatibilityMap": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      },
      "ForwardCompatibilityMap_subfield_empty_type": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                  ]
                }
              }
            }
          }
        }
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


# this schema is based on this issue: https://github.com/adswerve/target-bigquery/issues/3
invalid_schema_under_anyOf_empty_props_example_1 = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {


"sample_column_anyOf_empty_properties": {
  "anyOf": [
    {
      "items": {
        "properties": {
          "name": { "type": [ "null", "string" ] },
          "value": { "type": [ "null", "string" ] }
        },
        "type": [ "null", "object" ]
      },
      "type": [ "null", "array" ]
    },
    {
      "properties": {},
      "type": ["null", "object"]
    }
  ]
},
        "ForwardCompatibilityMap": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "KeyValuePairOfstringstring": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "type": [
                "null",
                "object"
              ],
              "additionalProperties": false,
              "properties": {
                "key": {
                  "type": [
                    "null",
                    "string"
                  ]
                },
                "value": {
                  "type": [
                    "null",
                    "string"
                  ]
                }
              }
            }
          }
        }
      }

    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_under_anyOf_empty_props_example_2 = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {


      "AudienceAdsBidAdjustment": {
        "type": [
          "null",
          "integer"
        ]
      },
      "BiddingScheme_missing_props_item_10": {
        "anyOf": [
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "InheritedBidStrategyType": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              },
              "TargetCpa": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "TargetRoas": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              },
              "TargetRoas": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "Type": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "MaxCpc": {
                "type": [
                  "null",
                  "object"
                ],
                "additionalProperties": false,
                "properties": {
                  "Amount": {
                    "type": [
                      "null",
                      "number"
                    ]
                  }
                }
              },
              "TargetAdPosition": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "TargetImpressionShare": {
                "type": [
                  "null",
                  "number"
                ]
              }
            }
          },
          {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
            }
          }
        ]
      }
    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_under_anyOf_deep_nested_empty_props = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {




      "Settings": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "Setting": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "anyOf": [
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Details": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "TargetSettingDetail": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": [
                              "null",
                              "object"
                            ],
                            "additionalProperties": false,
                            "properties": {
                              "CriterionTypeGroup": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "TargetAndBid": {
                                "type": [
                                  "boolean"
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "LocalInventoryAdsEnabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "Priority": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "SalesCountryCode": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "StoreId": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "BidBoostValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidMaxValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidOption": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "DomainName": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Language": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "PageFeedIds": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "long": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": "integer"
                          }
                        }
                      }
                    },
                    "Source": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      },


      "Settings_nested_anyof_missing_type_properties": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "Setting": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "anyOf": [
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Details": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "TargetSettingDetail": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": [
                              "null",
                              "object"
                            ],
                            "additionalProperties": false,
                            "properties": {
                              "CriterionTypeGroup": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "TargetAndBid_missing_type_properties": {

                                "properties": {}
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "LocalInventoryAdsEnabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "Priority": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "SalesCountryCode": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "StoreId": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "BidBoostValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidMaxValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidOption": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "DomainName": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Language": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "PageFeedIds": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "long": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": "integer"
                          }
                        }
                      }
                    },
                    "Source": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      }
    }
  },
  "key_properties": [
    "Id"
  ]
}"""


invalid_schema_under_anyOf_deep_nested_empty_type = """{
  "type": "SCHEMA",
  "stream": "campaigns",
  "schema": {
    "type": [
      "null",
      "object"
    ],
    "additionalProperties": false,
    "properties": {




      "Settings": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "Setting": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "anyOf": [
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Details": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "TargetSettingDetail": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": [
                              "null",
                              "object"
                            ],
                            "additionalProperties": false,
                            "properties": {
                              "CriterionTypeGroup": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "TargetAndBid": {
                                "type": [
                                  "boolean"
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "LocalInventoryAdsEnabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "Priority": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "SalesCountryCode": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "StoreId": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "BidBoostValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidMaxValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidOption": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "DomainName": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Language": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "PageFeedIds": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "long": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": "integer"
                          }
                        }
                      }
                    },
                    "Source": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      },


      "Settings_nested_anyof_missing_type_properties": {
        "type": [
          "null",
          "object"
        ],
        "properties": {
          "Setting": {
            "type": [
              "null",
              "array"
            ],
            "items": {
              "anyOf": [
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Details": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "TargetSettingDetail": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": [
                              "null",
                              "object"
                            ],
                            "additionalProperties": false,
                            "properties": {
                              "CriterionTypeGroup": {
                                "type": [
                                  "null",
                                  "string"
                                ]
                              },
                              "TargetAndBid_missing_type_properties": {
                                "type": [
                                ]
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "LocalInventoryAdsEnabled": {
                      "type": [
                        "null",
                        "boolean"
                      ]
                    },
                    "Priority": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "SalesCountryCode": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "StoreId": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "BidBoostValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidMaxValue": {
                      "type": [
                        "null",
                        "number"
                      ]
                    },
                    "BidOption": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "DomainName": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "Language": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "PageFeedIds": {
                      "type": [
                        "null",
                        "object"
                      ],
                      "properties": {
                        "long": {
                          "type": [
                            "null",
                            "array"
                          ],
                          "items": {
                            "type": "integer"
                          }
                        }
                      }
                    },
                    "Source": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                },
                {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Type": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              ]
            }
          }
        }
      }
    }
  },
  "key_properties": [
    "Id"
  ]
}"""