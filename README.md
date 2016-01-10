# CubeSensors Logstash Input Plugin

![Kibana](/clip_kibana.png?raw=true)

An input plugin for Logstash which collects cube data from your CubeSensors account.

## Dependencies

The plugin uses the OAuth gem: https://rubygems.org/gems/oauth

## Configuration

To configure the plugin you need first to get the OAuth credentials for your CubeSensors account.

If you have python installed then `scripts/cubesensors_get_access_token.py` may be of use.

Install the rauth dependency, run the script, follow the instructions, and you will get the OAuth app token and secret.


### Options

**debug**
If set to true debug logging it produced.

**consumer_key**
The OAuth consumer key.

**consumer_secret**
The OAuth consumer secret.

**token**
The OAuth app token.

**token_secret**
The OAuth app token secret.

**interval**
The poll interval in second.

### Example
	input {
		cubesensors {
			debug => false
			consumer_key => "abc123"
			consumer_secret => "acacacacac12121212"
			token => "aabbB34ccc"
			token_secret => "aB12fb"
			interval => 60
		}
	}

  filter {
    date {
    	match => [ "time", "ISO8601" ]
    }
  }

## Installing

    cd <location of logstash>
    ./bin/plugin.bat install <location of cubesensors plugin>/logstash-input-cubesensors-0.0.1.gem


## Building

If ruby is not installed then one can use logstash's JRuby:

    alias jruby=<location of logstashs>/vendor/jruby/bin/jruby.exe

Build the gem:

    cd <location of cubesensors plugin>
    jruby -S gem build logstash-input-cubesensors.gemspec

See also: https://github.com/logstash-plugins/logstash-input-example