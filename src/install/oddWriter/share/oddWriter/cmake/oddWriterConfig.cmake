# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_oddWriter_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED oddWriter_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(oddWriter_FOUND FALSE)
  elseif(NOT oddWriter_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(oddWriter_FOUND FALSE)
  endif()
  return()
endif()
set(_oddWriter_CONFIG_INCLUDED TRUE)

# output package information
if(NOT oddWriter_FIND_QUIETLY)
  message(STATUS "Found oddWriter: 0.0.0 (${oddWriter_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'oddWriter' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT oddWriter_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(oddWriter_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${oddWriter_DIR}/${_extra}")
endforeach()
