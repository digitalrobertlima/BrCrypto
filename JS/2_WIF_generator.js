var CryptoJS = require('cryptojs').Crypto
var bs58 = require('bs58')

var version = '80' //WIF Use

var chavePrivada = process.argv[2]

console.log('\n Bem-vindo usuário! Este programa exige um argumento de entrada para funcionar, caso a chave privada não tenha sido passada como argumento o endereço poderá ficar inválido e você perder tuas moedas.\n\n Este programa irá te auxiliar na geração de endereços WIF(Wallet Import Format) válidos.\n\n >>> PROGRAMA - DK <<<\n\n >>> GERADOR DE ENDEREÇOS WIF <<<\n\n (WALLET IMPORT FORMAT)\n')

console.log('Argumento de entrada: \n' + chavePrivada)

var versionEchave = version + chavePrivada

console.log('Versão: \n' + versionEchave)

var primeiroSHA = CryptoJS.SHA256(CryptoJS.util.hexToBytes(versionEchave))

console.log('primeiroSHA \n' + primeiroSHA)

var segundoSHA = CryptoJS.SHA256(CryptoJS.util.hexToBytes(primeiroSHA))

console.log('segundoSHA: \n' + segundoSHA)

var checksum = segundoSHA.substr(0,8)

console.log('checksum: \n' + checksum)

var wif = versionEchave + checksum

console.log('WIF: \n' + wif)


var wifFinal = bs58.encode(CryptoJS.util.hexToBytes(wif))

console.log('WIF Final: \n' + wifFinal)


