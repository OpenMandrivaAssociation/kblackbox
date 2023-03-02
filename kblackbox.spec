Name:		kblackbox
Version:	22.12.3
Release:	1
Epoch:		1
Summary:	Find atoms in a grid by shooting electrons
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kblackbox
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5DocTools)

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

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kblackbox --with-html
