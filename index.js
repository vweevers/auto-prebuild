'use strict';

var addon = require('bindings')('addon')
  , assert = require('assert')

assert.equal(addon.add(3, 5), 8)
console.log('ok')
