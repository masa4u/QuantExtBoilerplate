include(subdir)

SUBDIRLISTR(_modules "${CMAKE_CURRENT_LIST_DIR}")
SET(_modules ${_modules} ".")
set(source_list)
FIND_PACKAGE(QuantLib REQUIRED)
foreach(_module ${_modules})
    file(GLOB_RECURSE _local_source
            "${_module}/*.hpp"
            "${_module}/*.cpp"
            )
    set(source_list ${source_list} ${_local_source})
endforeach(_module)

add_executable(examples ${source_list})

target_link_libraries(examples
        QuantExt
        ${QuantLib_LIBRARY}
        ${VLD_LIBRARY}
        )