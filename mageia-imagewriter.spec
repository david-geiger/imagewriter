%define rname     imagewriter_mageia
%define oname     imagewriter

Name:	    mageia-imagewriter
Version:	1.10
Release:	%mkrel 1
Summary:	Utility for writing raw disk images & hybrid ISOs to USB keys
License:	GPLv2
Group:	  System/Configuration 
Url:		  https://github.com/david-geiger/imagewriter
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	qt4-devel
BuildRequires:	udisks2

%description
A graphical utility for writing raw disk images & hybrid ISOs to USB keys

Based on SUSE Studio Imagewriter

%prep
%setup -q
%apply_patches

# rename_icons(Otherwise conflict with the package usb-imagewriter)
for png in 128x128 64x64 32x32; do
mv ./icons/${png}/%{oname}.png ./icons/${png}/%{rname}.png
done

%build
qmake DEFINES=USEUDISKS2 PREFIX=%{buildroot}%{_prefix} imagewriter.pro
make CFLAGS="$RPM_OPT_FLAGS -DKIOSKHACK"

%install
%makeinstall_std
mkdir -p %{buildroot}%{_sbindir}
# rename_binary(Otherwise conflict with the package usb-imagewriter)
mv %{buildroot}%{_bindir}/%{oname} %{buildroot}%{_sbindir}/%{rname}
cp %{name}.desktop %{buildroot}%{_datadir}/applications

# Adjust for console-helper magic
pushd %{buildroot}%{_bindir}
ln -s consolehelper %{rname}
popd

%files
%doc COPYING
%{_bindir}/%{rname}
%{_sbindir}/%{rname}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{rname}.*


%changelog
