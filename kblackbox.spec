#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		kblackbox
Version:	25.08.2
Release:	%{?git:0.%{git}.}1
Summary:	Find atoms in a grid by shooting electrons
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://games.kde.org/game.php?game=kblackbox
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kblackbox/-/archive/%{gitbranch}/kblackbox-%{gitbranchd}.tar.bz2#/kblackbox-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kblackbox-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:  qt6-qtbase-theme-gtk3

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%rename plasma6-kblackbox

%description
KBlackbox is a game of hide and seek played on a grid of boxes where the
computer has hidden several balls. The position of the hidden balls can be
deduced by shooting beams into the box.

%files -f kblackbox.lang
%{_bindir}/kblackbox
%{_datadir}/metainfo/org.kde.kblackbox.appdata.xml
%{_datadir}/applications/org.kde.kblackbox.desktop
%{_iconsdir}/hicolor/*/apps/kblackbox.png
%{_datadir}/kblackbox
