# Code generated by smithy-python-codegen DO NOT EDIT.

import aws_cryptography_primitives.smithygenerated.smithy_to_dafny
import module_
from software_amazon_cryptography_primitives_internaldafny_types import (
    AESDecryptInput_AESDecryptInput as DafnyAESDecryptInput,
    AESEncryptInput_AESEncryptInput as DafnyAESEncryptInput,
    AesKdfCtrInput_AesKdfCtrInput as DafnyAesKdfCtrInput,
    DigestInput_DigestInput as DafnyDigestInput,
    ECDSASignInput_ECDSASignInput as DafnyECDSASignInput,
    ECDSAVerifyInput_ECDSAVerifyInput as DafnyECDSAVerifyInput,
    GenerateECDSASignatureKeyInput_GenerateECDSASignatureKeyInput as DafnyGenerateECDSASignatureKeyInput,
    GenerateRSAKeyPairInput_GenerateRSAKeyPairInput as DafnyGenerateRSAKeyPairInput,
    GenerateRandomBytesInput_GenerateRandomBytesInput as DafnyGenerateRandomBytesInput,
    GetRSAKeyModulusLengthInput_GetRSAKeyModulusLengthInput as DafnyGetRSAKeyModulusLengthInput,
    HMacInput_HMacInput as DafnyHMacInput,
    HkdfExpandInput_HkdfExpandInput as DafnyHkdfExpandInput,
    HkdfExtractInput_HkdfExtractInput as DafnyHkdfExtractInput,
    HkdfInput_HkdfInput as DafnyHkdfInput,
    KdfCtrInput_KdfCtrInput as DafnyKdfCtrInput,
    RSADecryptInput_RSADecryptInput as DafnyRSADecryptInput,
    RSAEncryptInput_RSAEncryptInput as DafnyRSAEncryptInput,
)

from .dafny_protocol import DafnyRequest

from .config import Config


async def _serialize_h_mac(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="HMac", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_HMacInput(input))

async def _serialize_generate_ecdsa_signature_key(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="GenerateECDSASignatureKey", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_GenerateECDSASignatureKeyInput(input))

async def _serialize_generate_random_bytes(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="GenerateRandomBytes", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_GenerateRandomBytesInput(input))

async def _serialize_generate_rsa_key_pair(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="GenerateRSAKeyPair", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_GenerateRSAKeyPairInput(input))

async def _serialize_hkdf_expand(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="HkdfExpand", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_HkdfExpandInput(input))

async def _serialize_hkdf(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="Hkdf", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_HkdfInput(input))

async def _serialize_get_rsa_key_modulus_length(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="GetRSAKeyModulusLength", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_GetRSAKeyModulusLengthInput(input))

async def _serialize_digest(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="Digest", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_DigestInput(input))

async def _serialize_hkdf_extract(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="HkdfExtract", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_HkdfExtractInput(input))

async def _serialize_aes_decrypt(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="AESDecrypt", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_AESDecryptInput(input))

async def _serialize_kdf_counter_mode(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="KdfCounterMode", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_KdfCtrInput(input))

async def _serialize_rsa_decrypt(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="RSADecrypt", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_RSADecryptInput(input))

async def _serialize_ecdsa_sign(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="ECDSASign", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_ECDSASignInput(input))

async def _serialize_ecdsa_verify(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="ECDSAVerify", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_ECDSAVerifyInput(input))

async def _serialize_aes_encrypt(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="AESEncrypt", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_AESEncryptInput(input))

async def _serialize_rsa_encrypt(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="RSAEncrypt", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_RSAEncryptInput(input))

async def _serialize_aes_kdf_counter_mode(input, config: Config) -> DafnyRequest:
    return DafnyRequest(operation_name="AesKdfCounterMode", dafny_operation_input=aws_cryptography_primitives.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_primitives_AesKdfCtrInput(input))
