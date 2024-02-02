Name:		plasma6-kblackbox
Version:	24.01.95
Release:	1
Summary:	Find atoms in a grid by shooting electrons
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kblackbox
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kblackbox-%{version}.tar.xz
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
%autosetup -p1 -n kblackbox-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kblackbox --with-html
