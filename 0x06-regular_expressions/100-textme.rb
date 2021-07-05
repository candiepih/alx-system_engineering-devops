#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\w+|\+\d+)|to:([\+0-9]+)|flags:(-?\d:-?\d:-?\d:-?\d:-?\d)/).join
