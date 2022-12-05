execute_process(
    COMMAND ${Python3_EXECUTABLE} -m autocoder -n ${CMAKE_CURRENT_BINARY_DIR}/autosrc
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    OUTPUT_VARIABLE AUTOMOD_SRC
)

message(STATUS ${AUTOMOD_SRC})

add_custom_command(
    OUTPUT ${AUTOMOD_SRC}
    COMMAND ${Python3_EXECUTABLE} -m autocoder ${CMAKE_CURRENT_BINARY_DIR}/autosrc
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
    DEPENDS ${AUTOCODE_SRC}
)

add_library(automod ${AUTOMOD_SRC})
target_include_directories(automod PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/autosrc)
# add_dependencies(automod automod-src)
