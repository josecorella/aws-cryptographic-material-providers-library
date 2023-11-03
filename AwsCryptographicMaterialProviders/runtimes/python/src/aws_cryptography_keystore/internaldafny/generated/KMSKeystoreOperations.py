import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure

assert "KMSKeystoreOperations" == __name__
KMSKeystoreOperations = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def AttemptKmsOperation_q(kmsConfiguration, encryptionContext):
        source8_ = kmsConfiguration
        if True:
            d_119___mcc_h0_ = source8_.kmsKeyArn
            d_120_arn_ = d_119___mcc_h0_
            return (d_120_arn_) == ((encryptionContext)[(Structure.default__).KMS__FIELD])

    @staticmethod
    def GenerateKey(encryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        d_121_generatorRequest_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextRequest
        d_121_generatorRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextRequest_GenerateDataKeyWithoutPlaintextRequest((kmsConfiguration).kmsKeyArn, Wrappers.Option_Some(encryptionContext), Wrappers.Option_None(), Wrappers.Option_Some(32), Wrappers.Option_Some(grantTokens))
        d_122_maybeGenerateResponse_: Wrappers.Result
        out10_: Wrappers.Result
        out10_ = (kmsClient).GenerateDataKeyWithoutPlaintext(d_121_generatorRequest_)
        d_122_maybeGenerateResponse_ = out10_
        d_123_generateResponse_: software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse
        d_124_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.GenerateDataKeyWithoutPlaintextResponse.default())()
        def lambda11_(d_125_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_125_e_)

        d_124_valueOrError0_ = (d_122_maybeGenerateResponse_).MapFailure(lambda11_)
        if (d_124_valueOrError0_).IsFailure():
            res = (d_124_valueOrError0_).PropagateFailure()
            return res
        d_123_generateResponse_ = (d_124_valueOrError0_).Extract()
        d_126_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_126_valueOrError1_ = Wrappers.default__.Need((True) and (((d_123_generateResponse_).KeyId).is_Some), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_126_valueOrError1_).IsFailure():
            res = (d_126_valueOrError1_).PropagateFailure()
            return res
        d_127_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_127_valueOrError2_ = Wrappers.default__.Need(((((d_123_generateResponse_).CiphertextBlob).is_Some) and ((len(((d_123_generateResponse_).CiphertextBlob).value)) == ((Structure.default__).KMS__GEN__KEY__NO__PLAINTEXT__LENGTH__32))) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_123_generateResponse_).CiphertextBlob).value)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")))
        if (d_127_valueOrError2_).IsFailure():
            res = (d_127_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_123_generateResponse_)
        return res
        return res

    @staticmethod
    def ReEncryptKey(ciphertext, sourceEncryptionContext, destinationEncryptionContext, kmsConfiguration, grantTokens, kmsClient):
        res: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        d_128_reEncryptRequest_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptRequest
        d_128_reEncryptRequest_ = software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptRequest_ReEncryptRequest(ciphertext, Wrappers.Option_Some(sourceEncryptionContext), Wrappers.Option_Some((kmsConfiguration).kmsKeyArn), (kmsConfiguration).kmsKeyArn, Wrappers.Option_Some(destinationEncryptionContext), Wrappers.Option_None(), Wrappers.Option_None(), Wrappers.Option_Some(grantTokens))
        d_129_maybeReEncryptResponse_: Wrappers.Result
        out11_: Wrappers.Result
        out11_ = (kmsClient).ReEncrypt(d_128_reEncryptRequest_)
        d_129_maybeReEncryptResponse_ = out11_
        d_130_reEncryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse
        d_131_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.ReEncryptResponse.default())()
        def lambda12_(d_132_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_132_e_)

        d_131_valueOrError0_ = (d_129_maybeReEncryptResponse_).MapFailure(lambda12_)
        if (d_131_valueOrError0_).IsFailure():
            res = (d_131_valueOrError0_).PropagateFailure()
            return res
        d_130_reEncryptResponse_ = (d_131_valueOrError0_).Extract()
        d_133_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_133_valueOrError1_ = Wrappers.default__.Need((((((d_130_reEncryptResponse_).SourceKeyId).is_Some) and (((d_130_reEncryptResponse_).KeyId).is_Some)) and ((((d_130_reEncryptResponse_).SourceKeyId).value) == ((kmsConfiguration).kmsKeyArn))) and ((((d_130_reEncryptResponse_).KeyId).value) == ((kmsConfiguration).kmsKeyArn)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from KMS GenerateDataKey:: Invalid Key Id")))
        if (d_133_valueOrError1_).IsFailure():
            res = (d_133_valueOrError1_).PropagateFailure()
            return res
        d_134_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_134_valueOrError2_ = Wrappers.default__.Need((((d_130_reEncryptResponse_).CiphertextBlob).is_Some) and (software_amazon_cryptography_services_kms_internaldafny_types.default__.IsValid__CiphertextType(((d_130_reEncryptResponse_).CiphertextBlob).value)), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS GeneratedDataKey: Invalid ciphertext")))
        if (d_134_valueOrError2_).IsFailure():
            res = (d_134_valueOrError2_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(d_130_reEncryptResponse_)
        return res
        return res

    @staticmethod
    def DecryptKey(encryptionContext, item, kmsConfiguration, grantTokens, kmsClient):
        output: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        d_135_maybeDecryptResponse_: Wrappers.Result
        out12_: Wrappers.Result
        out12_ = (kmsClient).Decrypt(software_amazon_cryptography_services_kms_internaldafny_types.DecryptRequest_DecryptRequest(((item)[(Structure.default__).BRANCH__KEY__FIELD]).B, Wrappers.Option_Some(encryptionContext), Wrappers.Option_Some(grantTokens), Wrappers.Option_Some((kmsConfiguration).kmsKeyArn), Wrappers.Option_None()))
        d_135_maybeDecryptResponse_ = out12_
        d_136_decryptResponse_: software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse
        d_137_valueOrError0_: Wrappers.Result = Wrappers.Result_Success.default(software_amazon_cryptography_services_kms_internaldafny_types.DecryptResponse.default())()
        def lambda13_(d_138_e_):
            return software_amazon_cryptography_keystore_internaldafny_types.Error_ComAmazonawsKms(d_138_e_)

        d_137_valueOrError0_ = (d_135_maybeDecryptResponse_).MapFailure(lambda13_)
        if (d_137_valueOrError0_).IsFailure():
            output = (d_137_valueOrError0_).PropagateFailure()
            return output
        d_136_decryptResponse_ = (d_137_valueOrError0_).Extract()
        d_139_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome_Pass.default()()
        d_139_valueOrError1_ = Wrappers.default__.Need((((d_136_decryptResponse_).Plaintext).is_Some) and ((32) == (len(((d_136_decryptResponse_).Plaintext).value))), software_amazon_cryptography_keystore_internaldafny_types.Error_KeyStoreException(_dafny.Seq("Invalid response from AWS KMS Decrypt: Key is not 32 bytes.")))
        if (d_139_valueOrError1_).IsFailure():
            output = (d_139_valueOrError1_).PropagateFailure()
            return output
        output = Wrappers.Result_Success(d_136_decryptResponse_)
        return output

