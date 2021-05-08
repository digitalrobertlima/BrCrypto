var CryptoJS = require('cryptojs').Crypto
var ec = require('eccrypto')

var chavePrivada = process.argv[2]

var chavePublica = ec.getPublic(Buffer.from(CryptoJS.util.hexToBytes(chavePrivada)))

console.log(CryptoJS.util.bytesToHex(chavePublica))
