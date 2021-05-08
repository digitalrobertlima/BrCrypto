var nomePrograma = '\n Seja muito bem-vindo usuário. Este programa te ajudará na geração de chaves privadas de 32 bytes.\n\n >>> PROGRAMA - DK <<<\n\n >>> GERADOR DE CHAVES PRIVADAS <<<\n >>> EM BYTES E HEXADECIMAL <<<'

console.log(nomePrograma)

var CryptoJS = require('cryptojs').Crypto

var chavePrivada = CryptoJS.util.randomBytes(32)

console.log('\nChave privada em Bytes:\n\n' + chavePrivada)

var chavePrivadaHex = CryptoJS.util.bytesToHex(chavePrivada)

console.log('\nChave privada em Hexadecimal:\n\n' + chavePrivadaHex)


