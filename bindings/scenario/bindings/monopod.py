# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _monopod
else:
    import _monopod

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _monopod.delete_SwigPyIterator

    def value(self):
        return _monopod.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _monopod.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _monopod.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _monopod.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _monopod.SwigPyIterator_equal(self, x)

    def copy(self):
        return _monopod.SwigPyIterator_copy(self)

    def next(self):
        return _monopod.SwigPyIterator_next(self)

    def __next__(self):
        return _monopod.SwigPyIterator___next__(self)

    def previous(self):
        return _monopod.SwigPyIterator_previous(self)

    def advance(self, n):
        return _monopod.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _monopod.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _monopod.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _monopod.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _monopod.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _monopod.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _monopod.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _monopod:
_monopod.SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _monopod.SHARED_PTR_DISOWN
import scenario.bindings.core
class Model(scenario.bindings.core.Model):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _monopod.Model_swiginit(self, _monopod.new_Model())
    __swig_destroy__ = _monopod.delete_Model

    def id(self):
        return _monopod.Model_id(self)

    def valid(self):
        r"""
        Check if the model is valid.

        :rtype: boolean
        :return: True if the model is valid, false otherwise.
        """
        return _monopod.Model_valid(self)

    def name(self):
        r"""
        Get the name of the model.

        :rtype: string
        :return: The name of the model.
        """
        return _monopod.Model_name(self)

    def dofs(self, *args):
        return _monopod.Model_dofs(self, *args)

    def get_joint(self, joint_name):
        r"""
        Get a joint belonging to the model.

        :type jointName: string
        :param jointName: The name of the joint.
        :raises: std::runtime_error if the joint does not exist.
        :rtype: :py:class:`Joint`
        :return: The desired joint.
        """
        return _monopod.Model_get_joint(self, joint_name)

    def joint_names(self, scoped=False):
        r"""
        Get the name of all the model's joints.

        :type scoped: boolean
        :param scoped: Scope the joint names with the model name,
            (e.g. ``mymodel::joint1``).
        :rtype: Tuple[string]
        :return: The list of joint names.
        """
        return _monopod.Model_joint_names(self, scoped)

    def joint_positions(self, *args):
        r"""
        Get the joint positions.

        :type jointNames: Tuple[string]
        :param jointNames: Optional vector of considered joints that also
            defines the joint serialization. By default, ``Model::jointNames`` is
            used.
        :rtype: Tuple[float]
        :return: The serialization of joint positions. The vector has as many
            elements as DoFs of the considered joints.
        """
        return _monopod.Model_joint_positions(self, *args)

    def joint_velocities(self, *args):
        r"""
        Get the joint velocities.

        :type jointNames: Tuple[string]
        :param jointNames: Optional vector of considered joints that also
            defines the joint serialization. By default, ``Model::jointNames`` is
            used.
        :rtype: Tuple[float]
        :return: The serialization of joint velocities. The vector has as many
            elements as DoFs of the considered joints.
        """
        return _monopod.Model_joint_velocities(self, *args)

    def joint_accelerations(self, *args):
        r"""
        Get the joint accelerations.

        :type jointNames: Tuple[string]
        :param jointNames: Optional vector of considered joints that also
            defines the joint serialization. By default, ``Model::jointNames`` is
            used.
        :rtype: Tuple[float]
        :return: The serialization of joint accelerations. The vector has as many
            elements as DoFs of the considered joints.
        """
        return _monopod.Model_joint_accelerations(self, *args)

    def set_joint_control_mode(self, *args):
        r"""
        Set the control mode of model joints.

        :type mode: int
        :param mode: The desired joint control mode.
        :type jointNames: Tuple[string]
        :param jointNames: Optional vector of considered joints that also
            defines the joint serialization. By default, ``Model::jointNames`` is
            used.
        :rtype: boolean
        :return: True for success, false otherwise.
        """
        return _monopod.Model_set_joint_control_mode(self, *args)

    def joints(self, *args):
        r"""
        Get the joints of the model.

        :type jointNames: Tuple[string]
        :param jointNames: Optional vector of considered joints. By default,
            ``Model::jointNames`` is used.
        :rtype: Tuple[Joint]
        :return: A vector of pointers to the joint objects.
        """
        return _monopod.Model_joints(self, *args)

    def set_joint_generalized_force_targets(self, *args):
        r"""
        Set the generalized force targets of the joints.

        :type forces: Tuple[float]
        :param forces: The vector with the joint generalized force targets. It
            must have as many elements as the considered joint DoFs.
        :type jointNames: Tuple[string]
        :param jointNames: Optional vector of considered joints. By default,
            ``Model::jointNames`` is used.
        :rtype: boolean
        :return: True for success, false otherwise.
        """
        return _monopod.Model_set_joint_generalized_force_targets(self, *args)

    def joint_generalized_force_targets(self, *args):
        r"""
        Get the generalized force targets of the joints.

        :type jointNames: Tuple[string]
        :param jointNames: Optional vector of considered joints. By default,
            ``Model::jointNames`` is used.
        :rtype: Tuple[float]
        :return: The generalized force targets of the joints.
        """
        return _monopod.Model_joint_generalized_force_targets(self, *args)

# Register Model in _monopod:
_monopod.Model_swigregister(Model)

class World(scenario.bindings.core.World):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _monopod.World_swiginit(self, _monopod.new_World())
    __swig_destroy__ = _monopod.delete_World

    def id(self):
        return _monopod.World_id(self)

    def valid(self):
        r"""
        Check if the world is valid.

        :rtype: boolean
        :return: True if the world is valid, false otherwise.
        """
        return _monopod.World_valid(self)

    def name(self):
        r"""
        Get the name of the world.

        :rtype: string
        :return: The name of the world.
        """
        return _monopod.World_name(self)

    def model_names(self):
        r"""
        Get the name of the models that are part of the world.

        :rtype: Tuple[string]
        :return: The list of model names.
        """
        return _monopod.World_model_names(self)

    def get_model(self, model_name):
        r"""
        Get a model part of the world.

        :type modelName: string
        :param modelName: The name of the model to get.
        :rtype: :py:class:`Model`
        :return: The model if it is part of the world, ``nullptr`` otherwise.
        """
        return _monopod.World_get_model(self, model_name)

    def models(self, *args):
        r"""
        Get the models of the world.

        :type modelNames: Tuple[string]
        :param modelNames: Optional vector of considered models. By default,
            ``World::modelNames`` is used.
        :rtype: std::vector< scenario::core::ModelPtr,std::allocator< scenario::core::ModelPtr > >
        :return: A vector of pointers to the model objects.
        """
        return _monopod.World_models(self, *args)

# Register World in _monopod:
_monopod.World_swigregister(World)



