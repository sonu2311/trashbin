var trimUndesiredFields = function(obj) {
  if (obj && obj.constructor === Object) {
    var output = {}
    for (var k in obj) {
      if (k.length == 0 || k[0] != '$') {
        output[k] = trimUndesiredFields(obj[k])
      }
    }
    return output
  } else if (obj instanceof Array) {
    var output = []
    for (var k in obj) {
      output.push(trimUndesiredFields(obj[k]))
    }
    return output
  } else {
    return obj
  }
}

var store_key = "data"

function save(data) {
  if (data) {
    localStorage[store_key] = JSON.stringify(trimUndesiredFields(data))
  } else {
    console.error("Invalid data stored")
  }
}

function load() {
  if (localStorage[store_key] === undefined) {
    return null
  } else {
    return JSON.parse(localStorage[store_key])
  }
}

function clear() {
  localStorage.removeItem(store_key)
}

