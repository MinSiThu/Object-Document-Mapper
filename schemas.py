from datetime import datetime

user_schema = {
    "model_name":"User",
    "model_name_lowercase":"user",
    "model_description":"a collection about user",
    "model_name_plural":"users",
    "model_created_time":datetime.utcnow(),
    "model_updated_time":datetime.utcnow(),

    "fields":[
        {
            "type":"String", 
            "attribute_name":"username",
        },
        {
            "type":"Text",
            "attribute_name":"password",
        },
        {
            "type":"Number",
            "attribute_name":"age",
        },
        {
            "type":"Boolean",
            "attribute_name":"agree to privacy policy",
        },
        {
            "type":"Date",
            "attribute_name":"birthday",
        },
        {
            "type":"Enumeration",
            "attribute_name":"hobbies",
            "predefined_values":["Swimming","Football",'Reading','Gaming','PingPong']
        },
        {
            "type":"JSON",
            "attribute_name":"anythingInJson",
        }
    ]
}

post_schema = {
    "model_name":"Post",
    "model_name_lowercase":"post",
    "model_description":"a collection about post",
    "model_name_plural":"posts",
    "model_created_time":datetime.utcnow(),
    "model_updated_time":datetime.utcnow(),

    "fields":[
        {
            "type":"String", 
            "attribute_name":"title",
        },
        {
            "type":"Text",
            "attribute_name":"content",
        },
        {
            "type":"Date",
            "attribute_name":"birthday",
        },
        {
            "type":"Enumeration",
            "attribute_name":"type_of_post",
            "predefined_values":["Swimming","Football",'Reading','Gaming','PingPong']
        },
        {
            "type":"JSON",
            "attribute_name":"anythingInJson",
        }
    ]
}
