# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.10.1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.10.1/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp"

# Include any dependencies generated for this target.
include CMakeFiles/stack_with_max.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/stack_with_max.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/stack_with_max.dir/flags.make

CMakeFiles/stack_with_max.dir/stack_with_max.cc.o: CMakeFiles/stack_with_max.dir/flags.make
CMakeFiles/stack_with_max.dir/stack_with_max.cc.o: stack_with_max.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/stack_with_max.dir/stack_with_max.cc.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/stack_with_max.dir/stack_with_max.cc.o -c "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/stack_with_max.cc"

CMakeFiles/stack_with_max.dir/stack_with_max.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/stack_with_max.dir/stack_with_max.cc.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/stack_with_max.cc" > CMakeFiles/stack_with_max.dir/stack_with_max.cc.i

CMakeFiles/stack_with_max.dir/stack_with_max.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/stack_with_max.dir/stack_with_max.cc.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/stack_with_max.cc" -o CMakeFiles/stack_with_max.dir/stack_with_max.cc.s

CMakeFiles/stack_with_max.dir/stack_with_max.cc.o.requires:

.PHONY : CMakeFiles/stack_with_max.dir/stack_with_max.cc.o.requires

CMakeFiles/stack_with_max.dir/stack_with_max.cc.o.provides: CMakeFiles/stack_with_max.dir/stack_with_max.cc.o.requires
	$(MAKE) -f CMakeFiles/stack_with_max.dir/build.make CMakeFiles/stack_with_max.dir/stack_with_max.cc.o.provides.build
.PHONY : CMakeFiles/stack_with_max.dir/stack_with_max.cc.o.provides

CMakeFiles/stack_with_max.dir/stack_with_max.cc.o.provides.build: CMakeFiles/stack_with_max.dir/stack_with_max.cc.o


# Object files for target stack_with_max
stack_with_max_OBJECTS = \
"CMakeFiles/stack_with_max.dir/stack_with_max.cc.o"

# External object files for target stack_with_max
stack_with_max_EXTERNAL_OBJECTS =

stack_with_max: CMakeFiles/stack_with_max.dir/stack_with_max.cc.o
stack_with_max: CMakeFiles/stack_with_max.dir/build.make
stack_with_max: CMakeFiles/stack_with_max.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable stack_with_max"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/stack_with_max.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/stack_with_max.dir/build: stack_with_max

.PHONY : CMakeFiles/stack_with_max.dir/build

CMakeFiles/stack_with_max.dir/requires: CMakeFiles/stack_with_max.dir/stack_with_max.cc.o.requires

.PHONY : CMakeFiles/stack_with_max.dir/requires

CMakeFiles/stack_with_max.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/stack_with_max.dir/cmake_clean.cmake
.PHONY : CMakeFiles/stack_with_max.dir/clean

CMakeFiles/stack_with_max.dir/depend:
	cd "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp" "/Users/TsungHsienLee/Google Drive/episolutions/EPIJudge/epi_judge_cpp/CMakeFiles/stack_with_max.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/stack_with_max.dir/depend
