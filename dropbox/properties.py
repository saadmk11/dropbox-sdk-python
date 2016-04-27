# -*- coding: utf-8 -*-
# Auto-generated by BabelAPI, do not modify.
"""
This namespace contains helper entities for property and property/template endpoints.
"""

try:
    from . import babel_validators as bv
except (SystemError, ValueError):
    # Catch errors raised when importing a relative module when not in a package.
    # This makes testing this file directly (outside of a package) easier.
    import babel_validators as bv

class GetPropertyTemplateArg(object):
    """
    :ivar template_id: An identifier for property template added by route
        properties/template/add.
    """

    __slots__ = [
        '_template_id_value',
        '_template_id_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 template_id=None):
        self._template_id_value = None
        self._template_id_present = False
        if template_id is not None:
            self.template_id = template_id

    @property
    def template_id(self):
        """
        An identifier for property template added by route
        properties/template/add.

        :rtype: str
        """
        if self._template_id_present:
            return self._template_id_value
        else:
            raise AttributeError("missing required field 'template_id'")

    @template_id.setter
    def template_id(self, val):
        val = self._template_id_validator.validate(val)
        self._template_id_value = val
        self._template_id_present = True

    @template_id.deleter
    def template_id(self):
        self._template_id_value = None
        self._template_id_present = False

    def __repr__(self):
        return 'GetPropertyTemplateArg(template_id={!r})'.format(
            self._template_id_value,
        )

class PropertyGroupTemplate(object):
    """
    Describes property templates that can be filled and associated with a file.

    :ivar name: A display name for the property template. Property template
        names can be up to 256 bytes.
    :ivar description: Description for new property template. Property template
        descriptions can be up to 1024 bytes.
    :ivar fields: This is a list of custom properties associated with a property
        template. There can be up to 64 properties in a single property
        template.
    """

    __slots__ = [
        '_name_value',
        '_name_present',
        '_description_value',
        '_description_present',
        '_fields_value',
        '_fields_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 name=None,
                 description=None,
                 fields=None):
        self._name_value = None
        self._name_present = False
        self._description_value = None
        self._description_present = False
        self._fields_value = None
        self._fields_present = False
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if fields is not None:
            self.fields = fields

    @property
    def name(self):
        """
        A display name for the property template. Property template names can be
        up to 256 bytes.

        :rtype: str
        """
        if self._name_present:
            return self._name_value
        else:
            raise AttributeError("missing required field 'name'")

    @name.setter
    def name(self, val):
        val = self._name_validator.validate(val)
        self._name_value = val
        self._name_present = True

    @name.deleter
    def name(self):
        self._name_value = None
        self._name_present = False

    @property
    def description(self):
        """
        Description for new property template. Property template descriptions
        can be up to 1024 bytes.

        :rtype: str
        """
        if self._description_present:
            return self._description_value
        else:
            raise AttributeError("missing required field 'description'")

    @description.setter
    def description(self, val):
        val = self._description_validator.validate(val)
        self._description_value = val
        self._description_present = True

    @description.deleter
    def description(self):
        self._description_value = None
        self._description_present = False

    @property
    def fields(self):
        """
        This is a list of custom properties associated with a property template.
        There can be up to 64 properties in a single property template.

        :rtype: list of [PropertyFieldTemplate]
        """
        if self._fields_present:
            return self._fields_value
        else:
            raise AttributeError("missing required field 'fields'")

    @fields.setter
    def fields(self, val):
        val = self._fields_validator.validate(val)
        self._fields_value = val
        self._fields_present = True

    @fields.deleter
    def fields(self):
        self._fields_value = None
        self._fields_present = False

    def __repr__(self):
        return 'PropertyGroupTemplate(name={!r}, description={!r}, fields={!r})'.format(
            self._name_value,
            self._description_value,
            self._fields_value,
        )

class GetPropertyTemplateResult(PropertyGroupTemplate):
    """
    The Property template for the specified template.
    """

    __slots__ = [
    ]

    _has_required_fields = True

    def __init__(self,
                 name=None,
                 description=None,
                 fields=None):
        super(GetPropertyTemplateResult, self).__init__(name,
                                                        description,
                                                        fields)

    def __repr__(self):
        return 'GetPropertyTemplateResult(name={!r}, description={!r}, fields={!r})'.format(
            self._name_value,
            self._description_value,
            self._fields_value,
        )

class ListPropertyTemplateIds(object):
    """
    :ivar template_ids: List of identifiers for templates added by route
        properties/template/add.
    """

    __slots__ = [
        '_template_ids_value',
        '_template_ids_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 template_ids=None):
        self._template_ids_value = None
        self._template_ids_present = False
        if template_ids is not None:
            self.template_ids = template_ids

    @property
    def template_ids(self):
        """
        List of identifiers for templates added by route
        properties/template/add.

        :rtype: list of [str]
        """
        if self._template_ids_present:
            return self._template_ids_value
        else:
            raise AttributeError("missing required field 'template_ids'")

    @template_ids.setter
    def template_ids(self, val):
        val = self._template_ids_validator.validate(val)
        self._template_ids_value = val
        self._template_ids_present = True

    @template_ids.deleter
    def template_ids(self):
        self._template_ids_value = None
        self._template_ids_present = False

    def __repr__(self):
        return 'ListPropertyTemplateIds(template_ids={!r})'.format(
            self._template_ids_value,
        )

class PropertyTemplateError(object):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar str template_not_found: Property template does not exist for given
        identifier.
    :ivar restricted_content: You do not have the permissions to modify this
        property template.
    :ivar other: An unspecified error.
    """

    __slots__ = ['_tag', '_value']

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    restricted_content = None
    # Attribute is overwritten below the class definition
    other = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    @classmethod
    def template_not_found(cls, val):
        """
        Create an instance of this class set to the ``template_not_found`` tag
        with value ``val``.

        :param str val:
        :rtype: PropertyTemplateError
        """
        return cls('template_not_found', val)

    def is_template_not_found(self):
        """
        Check if the union tag is ``template_not_found``.

        :rtype: bool
        """
        return self._tag == 'template_not_found'

    def is_restricted_content(self):
        """
        Check if the union tag is ``restricted_content``.

        :rtype: bool
        """
        return self._tag == 'restricted_content'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def get_template_not_found(self):
        """
        Property template does not exist for given identifier.

        Only call this if :meth:`is_template_not_found` is true.

        :rtype: str
        """
        if not self.is_template_not_found():
            raise AttributeError("tag 'template_not_found' not set")
        return self._value

    def __repr__(self):
        return 'PropertyTemplateError(%r, %r)' % (self._tag, self._value)

class ModifyPropertyTemplateError(PropertyTemplateError):
    """
    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar conflicting_property_names: A property field name already exists in
        the template.
    :ivar too_many_properties: There are too many properties in the changed
        template. The maximum number of properties per template is 32.
    :ivar too_many_templates: There are too many templates for the team.
    :ivar template_attribute_too_large: The template name, description or field
        names is too large.
    """

    __slots__ = ['_tag', '_value']

    # Attribute is overwritten below the class definition
    conflicting_property_names = None
    # Attribute is overwritten below the class definition
    too_many_properties = None
    # Attribute is overwritten below the class definition
    too_many_templates = None
    # Attribute is overwritten below the class definition
    template_attribute_too_large = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_conflicting_property_names(self):
        """
        Check if the union tag is ``conflicting_property_names``.

        :rtype: bool
        """
        return self._tag == 'conflicting_property_names'

    def is_too_many_properties(self):
        """
        Check if the union tag is ``too_many_properties``.

        :rtype: bool
        """
        return self._tag == 'too_many_properties'

    def is_too_many_templates(self):
        """
        Check if the union tag is ``too_many_templates``.

        :rtype: bool
        """
        return self._tag == 'too_many_templates'

    def is_template_attribute_too_large(self):
        """
        Check if the union tag is ``template_attribute_too_large``.

        :rtype: bool
        """
        return self._tag == 'template_attribute_too_large'

    def __repr__(self):
        return 'ModifyPropertyTemplateError(%r, %r)' % (self._tag, self._value)

class PropertyField(object):
    """
    :ivar name: This is the name or key of a custom property in a property
        template. File property names can be up to 256 bytes.
    :ivar value: Value of a custom property attached to a file. Values can be up
        to 1024 bytes.
    """

    __slots__ = [
        '_name_value',
        '_name_present',
        '_value_value',
        '_value_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 name=None,
                 value=None):
        self._name_value = None
        self._name_present = False
        self._value_value = None
        self._value_present = False
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def name(self):
        """
        This is the name or key of a custom property in a property template.
        File property names can be up to 256 bytes.

        :rtype: str
        """
        if self._name_present:
            return self._name_value
        else:
            raise AttributeError("missing required field 'name'")

    @name.setter
    def name(self, val):
        val = self._name_validator.validate(val)
        self._name_value = val
        self._name_present = True

    @name.deleter
    def name(self):
        self._name_value = None
        self._name_present = False

    @property
    def value(self):
        """
        Value of a custom property attached to a file. Values can be up to 1024
        bytes.

        :rtype: str
        """
        if self._value_present:
            return self._value_value
        else:
            raise AttributeError("missing required field 'value'")

    @value.setter
    def value(self, val):
        val = self._value_validator.validate(val)
        self._value_value = val
        self._value_present = True

    @value.deleter
    def value(self):
        self._value_value = None
        self._value_present = False

    def __repr__(self):
        return 'PropertyField(name={!r}, value={!r})'.format(
            self._name_value,
            self._value_value,
        )

class PropertyFieldTemplate(object):
    """
    Describe a single property field type which that can be part of a property
    template.

    :ivar name: This is the name or key of a custom property in a property
        template. File property names can be up to 256 bytes.
    :ivar description: This is the description for a custom property in a
        property template. File property description can be up to 1024 bytes.
    :ivar type: This is the data type of the value of this property. This type
        will be enforced upon property creation and modifications.
    """

    __slots__ = [
        '_name_value',
        '_name_present',
        '_description_value',
        '_description_present',
        '_type_value',
        '_type_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 name=None,
                 description=None,
                 type=None):
        self._name_value = None
        self._name_present = False
        self._description_value = None
        self._description_present = False
        self._type_value = None
        self._type_present = False
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type

    @property
    def name(self):
        """
        This is the name or key of a custom property in a property template.
        File property names can be up to 256 bytes.

        :rtype: str
        """
        if self._name_present:
            return self._name_value
        else:
            raise AttributeError("missing required field 'name'")

    @name.setter
    def name(self, val):
        val = self._name_validator.validate(val)
        self._name_value = val
        self._name_present = True

    @name.deleter
    def name(self):
        self._name_value = None
        self._name_present = False

    @property
    def description(self):
        """
        This is the description for a custom property in a property template.
        File property description can be up to 1024 bytes.

        :rtype: str
        """
        if self._description_present:
            return self._description_value
        else:
            raise AttributeError("missing required field 'description'")

    @description.setter
    def description(self, val):
        val = self._description_validator.validate(val)
        self._description_value = val
        self._description_present = True

    @description.deleter
    def description(self):
        self._description_value = None
        self._description_present = False

    @property
    def type(self):
        """
        This is the data type of the value of this property. This type will be
        enforced upon property creation and modifications.

        :rtype: PropertyType
        """
        if self._type_present:
            return self._type_value
        else:
            raise AttributeError("missing required field 'type'")

    @type.setter
    def type(self, val):
        self._type_validator.validate_type_only(val)
        self._type_value = val
        self._type_present = True

    @type.deleter
    def type(self):
        self._type_value = None
        self._type_present = False

    def __repr__(self):
        return 'PropertyFieldTemplate(name={!r}, description={!r}, type={!r})'.format(
            self._name_value,
            self._description_value,
            self._type_value,
        )

class PropertyGroup(object):
    """
    Collection of custom properties in filled property templates.

    :ivar template_id: A unique identifier for a property template type.
    :ivar fields: This is a list of custom properties associated with a file.
        There can be up to 32 properties for a template.
    """

    __slots__ = [
        '_template_id_value',
        '_template_id_present',
        '_fields_value',
        '_fields_present',
    ]

    _has_required_fields = True

    def __init__(self,
                 template_id=None,
                 fields=None):
        self._template_id_value = None
        self._template_id_present = False
        self._fields_value = None
        self._fields_present = False
        if template_id is not None:
            self.template_id = template_id
        if fields is not None:
            self.fields = fields

    @property
    def template_id(self):
        """
        A unique identifier for a property template type.

        :rtype: str
        """
        if self._template_id_present:
            return self._template_id_value
        else:
            raise AttributeError("missing required field 'template_id'")

    @template_id.setter
    def template_id(self, val):
        val = self._template_id_validator.validate(val)
        self._template_id_value = val
        self._template_id_present = True

    @template_id.deleter
    def template_id(self):
        self._template_id_value = None
        self._template_id_present = False

    @property
    def fields(self):
        """
        This is a list of custom properties associated with a file. There can be
        up to 32 properties for a template.

        :rtype: list of [PropertyField]
        """
        if self._fields_present:
            return self._fields_value
        else:
            raise AttributeError("missing required field 'fields'")

    @fields.setter
    def fields(self, val):
        val = self._fields_validator.validate(val)
        self._fields_value = val
        self._fields_present = True

    @fields.deleter
    def fields(self):
        self._fields_value = None
        self._fields_present = False

    def __repr__(self):
        return 'PropertyGroup(template_id={!r}, fields={!r})'.format(
            self._template_id_value,
            self._fields_value,
        )

class PropertyType(object):
    """
    Data type of the given property added. This endpoint is in beta and  only
    properties of type strings is supported.

    This class acts as a tagged union. Only one of the ``is_*`` methods will
    return true. To get the associated value of a tag (if one exists), use the
    corresponding ``get_*`` method.

    :ivar string: The associated property will be of type string. Unicode is
        supported.
    """

    __slots__ = ['_tag', '_value']

    _catch_all = 'other'
    # Attribute is overwritten below the class definition
    string = None
    # Attribute is overwritten below the class definition
    other = None

    def __init__(self, tag, value=None):
        assert tag in self._tagmap, 'Invalid tag %r.' % tag
        validator = self._tagmap[tag]
        if isinstance(validator, bv.Void):
            assert value is None, 'Void type union member must have None value.'
        elif isinstance(validator, (bv.Struct, bv.Union)):
            validator.validate_type_only(value)
        else:
            validator.validate(value)
        self._tag = tag
        self._value = value

    def is_string(self):
        """
        Check if the union tag is ``string``.

        :rtype: bool
        """
        return self._tag == 'string'

    def is_other(self):
        """
        Check if the union tag is ``other``.

        :rtype: bool
        """
        return self._tag == 'other'

    def __repr__(self):
        return 'PropertyType(%r, %r)' % (self._tag, self._value)

TemplateId_validator = bv.String(min_length=1, pattern=u'(/|ptid:).*')
GetPropertyTemplateArg._template_id_validator = TemplateId_validator
GetPropertyTemplateArg._all_field_names_ = set(['template_id'])
GetPropertyTemplateArg._all_fields_ = [('template_id', GetPropertyTemplateArg._template_id_validator)]

PropertyGroupTemplate._name_validator = bv.String()
PropertyGroupTemplate._description_validator = bv.String()
PropertyGroupTemplate._fields_validator = bv.List(bv.Struct(PropertyFieldTemplate))
PropertyGroupTemplate._all_field_names_ = set([
    'name',
    'description',
    'fields',
])
PropertyGroupTemplate._all_fields_ = [
    ('name', PropertyGroupTemplate._name_validator),
    ('description', PropertyGroupTemplate._description_validator),
    ('fields', PropertyGroupTemplate._fields_validator),
]

GetPropertyTemplateResult._all_field_names_ = PropertyGroupTemplate._all_field_names_.union(set([]))
GetPropertyTemplateResult._all_fields_ = PropertyGroupTemplate._all_fields_ + []

ListPropertyTemplateIds._template_ids_validator = bv.List(TemplateId_validator)
ListPropertyTemplateIds._all_field_names_ = set(['template_ids'])
ListPropertyTemplateIds._all_fields_ = [('template_ids', ListPropertyTemplateIds._template_ids_validator)]

PropertyTemplateError._template_not_found_validator = TemplateId_validator
PropertyTemplateError._restricted_content_validator = bv.Void()
PropertyTemplateError._other_validator = bv.Void()
PropertyTemplateError._tagmap = {
    'template_not_found': PropertyTemplateError._template_not_found_validator,
    'restricted_content': PropertyTemplateError._restricted_content_validator,
    'other': PropertyTemplateError._other_validator,
}

PropertyTemplateError.restricted_content = PropertyTemplateError('restricted_content')
PropertyTemplateError.other = PropertyTemplateError('other')

ModifyPropertyTemplateError._conflicting_property_names_validator = bv.Void()
ModifyPropertyTemplateError._too_many_properties_validator = bv.Void()
ModifyPropertyTemplateError._too_many_templates_validator = bv.Void()
ModifyPropertyTemplateError._template_attribute_too_large_validator = bv.Void()
ModifyPropertyTemplateError._tagmap = {
    'conflicting_property_names': ModifyPropertyTemplateError._conflicting_property_names_validator,
    'too_many_properties': ModifyPropertyTemplateError._too_many_properties_validator,
    'too_many_templates': ModifyPropertyTemplateError._too_many_templates_validator,
    'template_attribute_too_large': ModifyPropertyTemplateError._template_attribute_too_large_validator,
}
ModifyPropertyTemplateError._tagmap.update(PropertyTemplateError._tagmap)

ModifyPropertyTemplateError.conflicting_property_names = ModifyPropertyTemplateError('conflicting_property_names')
ModifyPropertyTemplateError.too_many_properties = ModifyPropertyTemplateError('too_many_properties')
ModifyPropertyTemplateError.too_many_templates = ModifyPropertyTemplateError('too_many_templates')
ModifyPropertyTemplateError.template_attribute_too_large = ModifyPropertyTemplateError('template_attribute_too_large')

PropertyField._name_validator = bv.String()
PropertyField._value_validator = bv.String()
PropertyField._all_field_names_ = set([
    'name',
    'value',
])
PropertyField._all_fields_ = [
    ('name', PropertyField._name_validator),
    ('value', PropertyField._value_validator),
]

PropertyFieldTemplate._name_validator = bv.String()
PropertyFieldTemplate._description_validator = bv.String()
PropertyFieldTemplate._type_validator = bv.Union(PropertyType)
PropertyFieldTemplate._all_field_names_ = set([
    'name',
    'description',
    'type',
])
PropertyFieldTemplate._all_fields_ = [
    ('name', PropertyFieldTemplate._name_validator),
    ('description', PropertyFieldTemplate._description_validator),
    ('type', PropertyFieldTemplate._type_validator),
]

PropertyGroup._template_id_validator = TemplateId_validator
PropertyGroup._fields_validator = bv.List(bv.Struct(PropertyField))
PropertyGroup._all_field_names_ = set([
    'template_id',
    'fields',
])
PropertyGroup._all_fields_ = [
    ('template_id', PropertyGroup._template_id_validator),
    ('fields', PropertyGroup._fields_validator),
]

PropertyType._string_validator = bv.Void()
PropertyType._other_validator = bv.Void()
PropertyType._tagmap = {
    'string': PropertyType._string_validator,
    'other': PropertyType._other_validator,
}

PropertyType.string = PropertyType('string')
PropertyType.other = PropertyType('other')

