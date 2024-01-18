import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import DafnyLibraries
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
import UUID
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
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring

# Module: AwsKmsMrkDiscoveryKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ToStringForRegion(arn, region):
        if AwsArnParsing.default__.IsMultiRegionAwsKmsArn(arn):
            return (arn).ToArnString(Wrappers.Option_Some(region))
        elif True:
            return (arn).ToString()

    @staticmethod
    def DiscoveryMatch(arn, discoveryFilter, region):
        pat_let_tv157_ = arn
        pat_let_tv158_ = arn
        def lambda60_(source24_):
            if source24_.is_None:
                return True
            elif True:
                d_650___mcc_h0_ = source24_.value
                d_651_filter_ = d_650___mcc_h0_
                return (((d_651_filter_).partition) == ((pat_let_tv157_).partition)) and (((pat_let_tv158_).account) in ((d_651_filter_).accountIds))

        return (lambda60_(discoveryFilter)) and (((region) == ((arn).region) if not(AwsArnParsing.default__.IsMultiRegionAwsKmsArn(arn)) else True))


class AwsKmsMrkDiscoveryKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._region: _dafny.Seq = _dafny.Seq({})
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsMrkDiscoveryKeyring"
    def OnEncrypt(self, input):
        out99_: Wrappers.Result
        out99_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out99_

    def OnDecrypt(self, input):
        out100_: Wrappers.Result
        out100_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out100_

    def ctor__(self, client, region, discoveryFilter, grantTokens):
        (self)._client = client
        (self)._region = region
        (self)._discoveryFilter = discoveryFilter
        (self)._grantTokens = grantTokens

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption is not supported with a Discovery Keyring.")))
        return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_652_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_652_materials_ = (input).materials
        d_653_encryptedDataKeys_: _dafny.Seq
        d_653_encryptedDataKeys_ = (input).encryptedDataKeys
        d_654_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_654_suite_ = ((input).materials).algorithmSuite
        d_655_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_655_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_652_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_655_valueOrError0_).IsFailure():
            output = (d_655_valueOrError0_).PropagateFailure()
            return output
        d_656_edkFilterTransform_: AwsKmsEncryptedDataKeyFilterTransform
        nw15_ = AwsKmsEncryptedDataKeyFilterTransform()
        nw15_.ctor__((self).region, (self).discoveryFilter)
        d_656_edkFilterTransform_ = nw15_
        d_657_edksToAttempt_: _dafny.Seq
        d_658_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out101_: Wrappers.Result
        out101_ = Actions.default__.DeterministicFlatMapWithResult(d_656_edkFilterTransform_, d_653_encryptedDataKeys_)
        d_658_valueOrError1_ = out101_
        if (d_658_valueOrError1_).IsFailure():
            output = (d_658_valueOrError1_).PropagateFailure()
            return output
        d_657_edksToAttempt_ = (d_658_valueOrError1_).Extract()
        d_659_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_659_valueOrError2_ = Wrappers.default__.Need((0) < (len(d_657_edksToAttempt_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Unable to decrypt data key: No Encrypted Data Keys found to match.")))
        if (d_659_valueOrError2_).IsFailure():
            output = (d_659_valueOrError2_).PropagateFailure()
            return output
        d_660_decryptAction_: AwsKmsEncryptedDataKeyDecryptor
        nw16_ = AwsKmsEncryptedDataKeyDecryptor()
        nw16_.ctor__(d_652_materials_, (self).client, (self).region, (self).grantTokens)
        d_660_decryptAction_ = nw16_
        d_661_outcome_: Wrappers.Result
        out102_: Wrappers.Result
        out102_ = Actions.default__.ReduceToSuccess(d_660_decryptAction_, d_657_edksToAttempt_)
        d_661_outcome_ = out102_
        def lambda61_(source25_):
            if source25_.is_Success:
                d_662___mcc_h0_ = source25_.value
                d_663_mat_ = d_662___mcc_h0_
                return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_663_mat_))
            elif True:
                d_664___mcc_h1_ = source25_.error
                d_665_errors_ = d_664___mcc_h1_
                return Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_665_errors_, _dafny.Seq("No Configured KMS Key was able to decrypt the Data Key. The list of encountered Exceptions is available via `list`.")))

        output = lambda61_(d_661_outcome_)
        return output
        return output

    @property
    def client(self):
        return self._client
    @property
    def region(self):
        return self._region
    @property
    def discoveryFilter(self):
        return self._discoveryFilter
    @property
    def grantTokens(self):
        return self._grantTokens

class AwsKmsEncryptedDataKeyFilterTransform(Actions.DeterministicActionWithResult, Actions.DeterministicAction):
    def  __init__(self):
        self._region: _dafny.Seq = _dafny.Seq({})
        self._discoveryFilter: Wrappers.Option = Wrappers.Option.default()()
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyFilterTransform"
    def ctor__(self, region, discoveryFilter):
        (self)._region = region
        (self)._discoveryFilter = discoveryFilter

    def Invoke(self, edk):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        if ((edk).keyProviderId) != (Constants.default__.PROVIDER__ID):
            res = Wrappers.Result_Success(_dafny.Seq([]))
            return res
        d_666_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_666_valueOrError0_ = Wrappers.default__.Need(UTF8.default__.ValidUTF8Seq((edk).keyProviderInfo), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Invalid AWS KMS encoding, provider info is not UTF8.")))
        if (d_666_valueOrError0_).IsFailure():
            res = (d_666_valueOrError0_).PropagateFailure()
            return res
        d_667_keyId_: _dafny.Seq
        d_668_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda62_(d_669_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_669_e_)

        d_668_valueOrError1_ = (UTF8.default__.Decode((edk).keyProviderInfo)).MapFailure(lambda62_)
        if (d_668_valueOrError1_).IsFailure():
            res = (d_668_valueOrError1_).PropagateFailure()
            return res
        d_667_keyId_ = (d_668_valueOrError1_).Extract()
        d_670_arn_: AwsArnParsing.AwsArn
        d_671_valueOrError2_: Wrappers.Result = None
        def lambda63_(d_672_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_672_e_)

        d_671_valueOrError2_ = (AwsArnParsing.default__.ParseAwsKmsArn(d_667_keyId_)).MapFailure(lambda63_)
        if (d_671_valueOrError2_).IsFailure():
            res = (d_671_valueOrError2_).PropagateFailure()
            return res
        d_670_arn_ = (d_671_valueOrError2_).Extract()
        d_673_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_673_valueOrError3_ = Wrappers.default__.Need((((d_670_arn_).resource).resourceType) == (_dafny.Seq("key")), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Only AWS KMS Keys supported")))
        if (d_673_valueOrError3_).IsFailure():
            res = (d_673_valueOrError3_).PropagateFailure()
            return res
        if not(default__.DiscoveryMatch(d_670_arn_, (self).discoveryFilter, (self).region)):
            res = Wrappers.Result_Success(_dafny.Seq([]))
            return res
        res = Wrappers.Result_Success(_dafny.Seq([Constants.AwsKmsEdkHelper_AwsKmsEdkHelper(edk, d_670_arn_)]))
        return res
        return res

    @property
    def region(self):
        return self._region
    @property
    def discoveryFilter(self):
        return self._discoveryFilter

class AwsKmsEncryptedDataKeyDecryptor(Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._materials: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials = None
        self._client: software_amazon_cryptography_services_kms_internaldafny_types.IKMSClient = None
        self._region: _dafny.Seq = _dafny.Seq({})
        self._grantTokens: _dafny.Seq = None
        pass

    def __dafnystr__(self) -> str:
        return "AwsKmsMrkDiscoveryKeyring.AwsKmsEncryptedDataKeyDecryptor"
    def ctor__(self, materials, client, region, grantTokens):
        (self)._materials = materials
        (self)._client = client
        (self)._region = region
        (self)._grantTokens = grantTokens

    def Invoke(self, helper):
        res: Wrappers.Result = None
        d_674_awsKmsKey_: _dafny.Seq
        d_674_awsKmsKey_ = default__.ToStringForRegion((helper).arn, (self).region)
        d_675___v0_: tuple
        d_676_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.tuple())()
        d_676_valueOrError0_ = AwsKmsUtils.default__.ValidateKmsKeyId(d_674_awsKmsKey_)
        if (d_676_valueOrError0_).IsFailure():
            res = (d_676_valueOrError0_).PropagateFailure()
            return res
        d_675___v0_ = (d_676_valueOrError0_).Extract()
        d_677_kmsUnwrap_: AwsKmsKeyring.KmsUnwrapKeyMaterial
        nw17_ = AwsKmsKeyring.KmsUnwrapKeyMaterial()
        nw17_.ctor__((self).client, d_674_awsKmsKey_, (self).grantTokens)
        d_677_kmsUnwrap_ = nw17_
        d_678_unwrapOutputRes_: Wrappers.Result
        out103_: Wrappers.Result
        out103_ = EdkWrapping.default__.UnwrapEdkMaterial(((helper).edk).ciphertext, (self).materials, d_677_kmsUnwrap_)
        d_678_unwrapOutputRes_ = out103_
        d_679_unwrapOutput_: EdkWrapping.UnwrapEdkMaterialOutput
        d_680_valueOrError1_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.UnwrapEdkMaterialOutput.default(AwsKmsKeyring.KmsUnwrapInfo.default()))()
        d_680_valueOrError1_ = d_678_unwrapOutputRes_
        if (d_680_valueOrError1_).IsFailure():
            res = (d_680_valueOrError1_).PropagateFailure()
            return res
        d_679_unwrapOutput_ = (d_680_valueOrError1_).Extract()
        res = Materials.default__.DecryptionMaterialsAddDataKey((self).materials, (d_679_unwrapOutput_).plaintextDataKey, (d_679_unwrapOutput_).symmetricSigningKey)
        return res

    @property
    def materials(self):
        return self._materials
    @property
    def client(self):
        return self._client
    @property
    def region(self):
        return self._region
    @property
    def grantTokens(self):
        return self._grantTokens
