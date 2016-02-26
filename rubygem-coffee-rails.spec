Name     : rubygem-coffee-rails
Version  : 4.1.0
Release  : 6
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
BuildRequires : rubygem-thor
BuildRequires : rubygem-thread_safe
BuildRequires : rubygem-tzinfo

# Requirements to solve javascript erro
BuildRequires : rubygem-libv8
BuildRequires : rubygem-ref
BuildRequires : rubygem-ronn
BuildRequires : rubygem-therubyracer

%description
# Coffee-Rails
CoffeeScript adapter for the Rails asset pipeline. Also adds support to use CoffeeScript to respond to JavaScript requests (use .js.coffee views).

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

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/coffee-rails-4.1.1
# Disable Bundler.
# sed -i '/require .bundler\/setup./ s/^/#/' test/test_helper.rb

# Explicitly require ActionController to workaround "uninitialized constant
# ActionController::Live" issue.
# https://github.com/rails/rails/issues/15918
# Explicitly require Shellwords to avoid "undefined method `shellescape'" error.
# https://github.com/rails/rails/issues/15919
ruby -raction_controller -rshellwords -I.:test:lib -e 'Dir.glob("test/**/*_test.rb").each {|t| require t}' ||:
popd


%files
%defattr(-,root,root,-)
%exclude /usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/test/tmp/
/usr/lib64/ruby/gems/2.2.0/cache/coffee-rails-4.1.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/ActionView/cdesc-ActionView.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/Coffee/Generators/AssetsGenerator/cdesc-AssetsGenerator.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/Coffee/Generators/AssetsGenerator/copy_coffee-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/Coffee/Generators/cdesc-Generators.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/Coffee/Rails/Engine/cdesc-Engine.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/Coffee/Rails/TemplateHandler/call-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/Coffee/Rails/TemplateHandler/cdesc-TemplateHandler.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/Coffee/Rails/TemplateHandler/erb_handler-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/Coffee/Rails/cdesc-Rails.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/Coffee/cdesc-Coffee.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/coffee-rails-4.1.1/ri/lib/rails/generators/coffee/assets/templates/page-javascript_coffee.ri
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/README.md
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/lib/assets/javascripts/coffee-script.js.erb
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/lib/coffee-rails.rb
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/lib/coffee/rails/engine.rb
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/lib/coffee/rails/template_handler.rb
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/lib/coffee/rails/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/lib/rails/generators/coffee/assets/assets_generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/coffee-rails-4.1.1/lib/rails/generators/coffee/assets/templates/javascript.coffee
/usr/lib64/ruby/gems/2.2.0/specifications/coffee-rails-4.1.1.gemspec
