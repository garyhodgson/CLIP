To install  plugin:

    cd <location of logstash>
    ./bin/plugin.bat install <location of cubesensors plugin>/logstash-input-cubesensors-0.0.1.gem



To build the plugin:


If ruby is not installed then one can use logstash's JRuby:

    alias jruby=<location of logstash>/vendor/jruby/bin/jruby.exe


Build the gem:

    cd <location of cubesensors plugin>
    jruby -S gem build logstash-input-cubesensors.gemspec


See also: https://github.com/logstash-plugins/logstash-input-example