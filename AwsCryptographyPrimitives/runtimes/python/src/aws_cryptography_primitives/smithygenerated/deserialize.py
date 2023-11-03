# Code generated by smithy-python-codegen DO NOT EDIT.

import aws_cryptography_primitives.smithygenerated.dafny_to_smithy
import module_
from software_amazon_cryptography_primitives_internaldafny_types import (
#     AESDecryptOutput_AESDecryptOutput as DafnyAESDecryptOutput,
#     AESEncryptOutput_AESEncryptOutput as DafnyAESEncryptOutput,
#     AesKdfCtrOutput_AesKdfCtrOutput as DafnyAesKdfCtrOutput,
#     DigestOutput_DigestOutput as DafnyDigestOutput,
#     ECDSASignOutput_ECDSASignOutput as DafnyECDSASignOutput,
#     ECDSAVerifyOutput_ECDSAVerifyOutput as DafnyECDSAVerifyOutput,
    Error,
    Error_AwsCryptographicPrimitivesError,
#     GenerateECDSASignatureKeyOutput_GenerateECDSASignatureKeyOutput as DafnyGenerateECDSASignatureKeyOutput,
#     GenerateRSAKeyPairOutput_GenerateRSAKeyPairOutput as DafnyGenerateRSAKeyPairOutput,
#     GenerateRandomBytesOutput_GenerateRandomBytesOutput as DafnyGenerateRandomBytesOutput,
#     GetRSAKeyModulusLengthOutput_GetRSAKeyModulusLengthOutput as DafnyGetRSAKeyModulusLengthOutput,
#     HMacOutput_HMacOutput as DafnyHMacOutput,
#     HkdfExpandOutput_HkdfExpandOutput as DafnyHkdfExpandOutput,
#     HkdfExtractOutput_HkdfExtractOutput as DafnyHkdfExtractOutput,
#     HkdfOutput_HkdfOutput as DafnyHkdfOutput,
#     KdfCtrOutput_KdfCtrOutput as DafnyKdfCtrOutput,
#     RSADecryptOutput_RSADecryptOutput as DafnyRSADecryptOutput,
#     RSAEncryptOutput_RSAEncryptOutput as DafnyRSAEncryptOutput,
)
from typing import Any

from .dafny_protocol import DafnyResponse
from .errors import (
    AwsCryptographicPrimitivesError,
    CollectionOfErrors,
    OpaqueError,
    ServiceError,
)

from .config import Config


async def _deserialize_h_mac(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_HMacOutput(input.value)

async def _deserialize_generate_ecdsa_signature_key(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_GenerateECDSASignatureKeyOutput(input.value)

async def _deserialize_generate_random_bytes(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_GenerateRandomBytesOutput(input.value)

async def _deserialize_generate_rsa_key_pair(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_GenerateRSAKeyPairOutput(input.value)

async def _deserialize_hkdf_expand(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_HkdfExpandOutput(input.value)

async def _deserialize_hkdf(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_HkdfOutput(input.value)

async def _deserialize_get_rsa_key_modulus_length(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_GetRSAKeyModulusLengthOutput(input.value)

async def _deserialize_digest(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_DigestOutput(input.value)

async def _deserialize_hkdf_extract(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_HkdfExtractOutput(input.value)

async def _deserialize_aes_decrypt(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_AESDecryptOutput(input.value)

async def _deserialize_kdf_counter_mode(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_KdfCtrOutput(input.value)

async def _deserialize_rsa_decrypt(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_RSADecryptOutput(input.value)

async def _deserialize_ecdsa_sign(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_ECDSASignOutput(input.value)

async def _deserialize_ecdsa_verify(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_ECDSAVerifyOutput(input.value)

async def _deserialize_aes_encrypt(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_AESEncryptOutput(input.value)

async def _deserialize_rsa_encrypt(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_RSAEncryptOutput(input.value)

async def _deserialize_aes_kdf_counter_mode(input: DafnyResponse, config: Config):

  if input.IsFailure():
    return await _deserialize_error(input.error)
  return aws_cryptography_primitives.smithygenerated.dafny_to_smithy.DafnyToSmithy_aws_cryptography_primitives_AesKdfCtrOutput(input.value)

async def _deserialize_error(error: Error) -> ServiceError:
    if error.is_Opaque:
      return OpaqueError(obj=error.obj)
    elif error.is_CollectionOfErrors:
      return CollectionOfErrors(message=error.message, list=error.list)
    elif error.is_AwsCryptographicPrimitivesError:
      return AwsCryptographicPrimitivesError(message=error.message)
    else:
        return OpaqueError(obj=error)
