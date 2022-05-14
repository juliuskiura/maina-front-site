from wagtail.core import hooks
from draftjs_exporter.dom import DOM
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler
from wagtail.admin.rich_text.converters.html_to_contentstate import ExternalLinkElementHandler, PageLinkElementHandler




@hooks.register('register_rich_text_features')
def register_code_styling(features):

    feature_name = 'code'
    type_ = '_CODE'
    tag = 'code'

    control = {
        'type': type_,
        'label': '</>',
        'description': 'Code',

    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format':{tag: InlineStyleElementHandler(type_)},
        'to_database_format':{'style_map': {type_: tag}},
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    features.default_features.append(feature_name)







@hooks.register('register_rich_text_features')
def register_center_text_feature(features):
    
    feature_name ='Center'
    type_ = 'CENTERTEXT'
    tag = 'div'

    control = {
        'type': type_,
        'label': '≡',
        'description': 'Centering text',
        'style': {
            'display':'block',
            'text-align':'center',
        },
       
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format':{tag: InlineStyleElementHandler(type_)},
        'to_database_format':{
            'style_map': {
                type_: {
                    'element': tag,
                    'props':{
                        'class':'d-block text-center',                        
                    }
                }
                }
            },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)
    features.default_features.append(feature_name)


    # <h2 class="card-title font-weight-bold mb-1"> Welcome to Vuexy! 👋 </h2>
@hooks.register('register_rich_text_features')
def register_cta_text_feature(features):
    feature_name ='CTA'
    type_ = 'LINK'
    tag = 'div'
    
    control = {
        'type': type_,
        'label': '📌',
        'description': 'Centering text',
      
        'style': {
            'display':'block',       
        },
       
    }
    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    
    db_conversion = {
        'from_database_format':{tag: ExternalLinkElementHandler(type_)},
        'a[linktype="page"]': PageLinkElementHandler(type_),
        'to_database_format':{
            'style_map': {
                type_: {
                    'element': tag,
                    'props':{
                        'class':'d-block blog-cta',                        
                    }
                }
                }
            },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)
    features.default_features.append(feature_name)

 