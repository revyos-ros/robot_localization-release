%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-robot-localization
Version:        2.7.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS robot_localization package

License:        BSD
URL:            http://ros.org/wiki/robot_localization
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-noetic-cmake-modules
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-diagnostic-updater
Requires:       ros-noetic-eigen-conversions
Requires:       ros-noetic-geographic-msgs
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-message-filters
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-tf2
Requires:       ros-noetic-tf2-geometry-msgs
Requires:       ros-noetic-tf2-ros
Requires:       ros-noetic-xmlrpcpp
Requires:       yaml-cpp-devel
BuildRequires:  GeographicLib-devel
BuildRequires:  eigen3-devel
BuildRequires:  python3-catkin_pkg
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-diagnostic-msgs
BuildRequires:  ros-noetic-diagnostic-updater
BuildRequires:  ros-noetic-eigen-conversions
BuildRequires:  ros-noetic-geographic-msgs
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-rosbag
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-rosunit
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-tf2
BuildRequires:  ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-tf2-ros
BuildRequires:  ros-noetic-xmlrpcpp
BuildRequires:  yaml-cpp-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Provides nonlinear state estimation through sensor fusion of an abritrary number
of sensors.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Dec 17 2020 Tom Moore <ayrton04@gmail.com> - 2.7.1-1
- Autogenerated by Bloom

* Wed Jun 03 2020 Tom Moore <ayrton04@gmail.com> - 2.6.8-2
- Autogenerated by Bloom

* Wed Jun 03 2020 Tom Moore <ayrton04@gmail.com> - 2.6.8-1
- Autogenerated by Bloom

