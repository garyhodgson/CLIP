Gem::Specification.new do |s|
  s.name = 'logstash-input-cubesensors'
  s.version = '0.0.1'
  s.licenses = ['']
  s.summary = "CubeSensors Logstash Input Plugin."
  s.description = "This gem is a logstash plugin required to be installed on top of the Logstash core pipeline using $LS_HOME/bin/plugin install gemname. This gem is not a stand-alone program."
  s.authors = ["peyerc", "g.hodgson"]
  s.homepage = "https://github.com/garyhodgson/CLIP"
  s.require_paths = ["lib"]

  # Files
  s.files = Dir['lib/**/*','*.gemspec','Gemfile']

  # Special flag to let us know this is actually a logstash plugin
  s.metadata = { "logstash_plugin" => "true", "logstash_group" => "input" }

  # Gem dependencies
  s.add_runtime_dependency "logstash-core", ">= 2.0.0", "< 3.0.0"
  s.add_runtime_dependency 'logstash-codec-json', ">= 2.0.0", "< 3.0.0"
  s.add_runtime_dependency 'oauth', '~> 0'

end
