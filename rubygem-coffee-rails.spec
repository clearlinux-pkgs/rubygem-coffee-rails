#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-coffee-rails
Version  : 4.1.1
Release  : 10
URL      : https://rubygems.org/downloads/coffee-rails-4.1.1.gem
Source0  : https://rubygems.org/downloads/coffee-rails-4.1.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-actionpack
BuildRequires : rubygem-actionview
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-builder
BuildRequires : rubygem-bundler
BuildRequires : rubygem-coffee-script
BuildRequires : rubygem-coffee-script-source
BuildRequires : rubygem-erubis
BuildRequires : rubygem-execjs
BuildRequires : rubygem-i18n
BuildRequires : rubygem-libv8
BuildRequires : rubygem-loofah
BuildRequires : rubygem-mini_portile
BuildRequires : rubygem-minitest
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rack
BuildRequires : rubygem-rack-test
BuildRequires : rubygem-rails
BuildRequires : rubygem-rails-deprecated_sanitizer
BuildRequires : rubygem-rails-dom-testing
BuildRequires : rubygem-rails-html-sanitizer
BuildRequires : rubygem-railties
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-ref
BuildRequires : rubygem-ronn
BuildRequires : rubygem-therubyracer
BuildRequires : rubygem-thor
BuildRequires : rubygem-thread_safe
BuildRequires : rubygem-tzinfo

%description
# Coffee-Rails
CoffeeScript adapter for the Rails asset pipeline. Also adds support to use CoffeeScript to respond to JavaScript requests (use `.coffee` views).

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n coffee-rails-4.1.1
gem spec %{SOURCE0} -l --ruby > rubygem-coffee-rails.gemspec

%build
gem build rubygem-coffee-rails.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
coffee-rails-4.1.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/coffee-rails-4.1.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/lib/assets/javascripts/coffee-script.js.erb
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/lib/coffee-rails.rb
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/lib/coffee/rails/engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/lib/coffee/rails/template_handler.rb
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/lib/coffee/rails/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/lib/rails/generators/coffee/assets/assets_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/coffee-rails-4.1.1/lib/rails/generators/coffee/assets/templates/javascript.coffee
/usr/lib64/ruby/gems/2.3.0/specifications/coffee-rails-4.1.1.gemspec
