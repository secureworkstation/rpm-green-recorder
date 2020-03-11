%global owner damianmoore
%global commit d147f5b8b1b0fbe713624011389cdc6d57b8afce
#%%define _unpackaged_files_terminate_build 0 

Name: green-recorder
Summary: A simple yet functional desktop recorder for Linux systems. Supports both Xorg server and Wayland (GNOME).
URL: https://github.com/damianmoore/green-recorder/
Version: 3.2.2
Release: 200.gitd147f5b
Source: https://github.com/%{owner}/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
License: GPLv3
BuildArch: noarch
BuildRequires: python3
BuildRequires: python
BuildRequires: python3-devel
Requires: python3
Requires: python3-pydbus
Requires: ffmpeg
Requires: gawk
Requires: libappindicator-gtk3
Requires: python3-urllib3
Requires: python3-configparser
Requires: pulseaudio
Requires: ImageMagick
Requires: xdg-utils

%description
A simple desktop recorder for Linux systems. Supports both Xorg server and Wayland (GNOME).

%prep
%autosetup -n %{name}-%{commit}

%build
python3 setup.py build

%install
python3 setup.py install -O1 --root=$RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/locale/*/LC_MESSAGES/green-recorder.mo

%changelog
* Thu Mar 12 2019 secureworkstation - 3.2.2
- Rebase to damianmoore's GitHub branch which builds with Python 3

* Sun Feb 17 2019 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.2.2
- Various bug fixes.

* Sun Feb 10 2019 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.2.1
- Fixed the stop button not working.
- Fixed the options list missing icon.

* Mon Feb 04 2019 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.2
- Enhanced the UI.
- Restored system tray icon.
- Removed preferences window. Now the program will use the same options just when you closed it last time.
- Now the program auto-hides its window on recording, and auto-shows when it's stopped.
- Added a stop notification when recording stops.
- Added various translations.
- Various bug fixes.

* Sun Oct 29 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.1
- Removed system tray icon and added close button.
- Fixed #68, #70 and #77.

* Fri Oct 20 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.6
- Fixed #73.

* Thu Oct 12 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.5
- Fixed small issues evreywhere.
- Restructured UI.

* Tue Aug 08 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.4
- Fixed small issues evreywhere.
- Removed Wayland pipeline editing option.
- Reworked UI.
- Updated translation template.
- Fixed applet on MATE.

* Mon Aug 07 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.3
- Fixed small issues.

* Sun Aug 06 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.2
- Fixed #46.

* Sun Aug 06 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.1.1
- A small fix for UI warning.

* Sun Aug 06 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0.1
- A small fix for UI warning.

* Mon Aug 06 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 3.0
- GIF format support is now available!
- Added ability to choose the audio input source.
- Preferences window was added to allow setting default values. You can now also edit the default Wayland pipeline.
- Reorganized the code and made it much clearer and simpler.
- Reorganized the graphical user interface.
- Added play button to easily enable playing the recorded video.
- Fixed a bug in recording video only or audio only on Wayland.
- Created a better ffmpeg detection on Xorg.
- Introduced a better detection method for the running display server, adding possibility to support other servers in the future with no problem.
- Various fixes and edits everywhere.

* Tue Jun 06 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.2
- Added localization support.
- Added Arabic language.
- Changed window opacity to 1.00

* Thu Apr 27 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.1.5
- Fix bug #25.

* Thu Apr 27 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.1.4
- Some various fixes.

* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.1-1
- Fix Spec file (mhsabbagh@outlook.com)
- Version 2.0 (mhsabbagh@outlook.com)

* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com>
- Fix Spec file (mhsabbagh@outlook.com)
- Version 2.0 (mhsabbagh@outlook.com)

* Sun Mar 05 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 2.0-1
- Added Wayland Support (GNOME Session).
- Added ability to select a specific window.
- Added ability to select a specific area.
- Added ability to show/hide mouse cursor.
- Added ability to follow mouse cursor.
- Added ability run a command after finishing recording.
- Indicator now checking for ffmpeg before running.
- Fixed some issues about multi-recordings.
- Update green-recorder (gort818@gmail.com)
- Update finding the video folder (gort818@gmail.com)
- Update green-recorder (gort818@gmail.com)
- Fix hidden icon from status bar in Wayland session (moceap@hotmail.com)

* Tue Feb 14 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 1.1.2-1
- new package built with tito

* Tue Feb 14 2017 M.Hanny Sabbagh <mhsabbagh@outlook.com> 1.1.2
- Version 1.1.2. 
