import platform
import ctypes

if platform.system() == 'Windows':
	__NomeBiblioteca = 'DarumaFrameWork'
	__ExtBiblioteca = '.dll'
	__PathBiblioteca = ''
	__Biblioteca = ctypes.windll.LoadLibrary(__PathBiblioteca + __NomeBiblioteca + __ExtBiblioteca)
else:
	__NomeBiblioteca = 'libDarumaFramework'
	__ExtBiblioteca = '.so'
	__PathBiblioteca = '/usr/local/lib/'
	__Biblioteca = ctypes.CDLL.LoadLibrary(__PathBiblioteca + __NomeBiblioteca + __ExtBiblioteca)

'''
class DarumaFramework(self):

	_Biblioteca = None
	_PathBiblioteca = None
	_NomeBiblioteca = None
	_ExtBiblioteca = None

	def __init__(self):
		if platform.system() == 'Windows':
			__NomeBiblioteca = 'DarumaFrameWork'
			__ExtBiblioteca = '.dll'
			__PathBiblioteca = 'c:\\'
			__Biblioteca = ctypes.windll(_PathBiblioteca + _NomeBiblioteca + _ExtBiblioteca)
		else:
			__NomeBiblioteca = 'libDarumaFramework'
			__ExtBiblioteca = '.so'
			__PathBiblioteca = '/usr/local/lib/'
			__Biblioteca = ctypes.CDLL.LoadLibrary(_PathBiblioteca + _NomeBiblioteca + _ExtBiblioteca)
'''

def eAbrirSerial_Daruma(StrPorta, StrVelocidade):
	return __Biblioteca.eAbrirSerial_Daruma(StrPorta.encode('ascii'), StrVelocidade.encode('ascii'))

def eFecharSerial_Daruma():
	return __Biblioteca.eFecharSerial_Daruma()

def tEnviarDados_Daruma(StrInformacao, iTamanhoBytes):
	return __Biblioteca.tEnviarDados_Daruma(StrInformacao.encode('ascii'), iTamanhoBytes)

def rReceberDados_Daruma(StrInformacao):
	return __Biblioteca.rReceberDados_Daruma(byref(StrInformacao.encode('ascii')))

		# Bilhete de passagem
def confCFBPProgramarUF_ECF_Daruma(pszUF):
	return __Biblioteca.confCFBPProgramarUF_ECF_Daruma(pszUF.encode('ascii'))

def iCFBPAbrir_ECF_Daruma(pszOrigem, pszDestino, pszUFDestino, pszPercurso, pszPrestadora, pszPlataforma, pszPoltrona, pszModalidadetransp, pszCategoriaTransp, pszDataEmbarque, pszRGPassageiro, pszNomePassageiro, pszEnderecoPassageiro):
	return __Biblioteca.iCFBPAbrir_ECF_Daruma(
				pszOrigem.encode('ascii'),
				pszDestino.encode('ascii'),
				pszUFDestino.encode('ascii'),
				pszPercurso.encode('ascii'),
				pszPrestadora.encode('ascii'),
				pszPlataforma.encode('ascii'),
				pszPoltrona.encode('ascii'),
				pszModalidadetransp.encode('ascii'),
				pszCategoriaTransp.encode('ascii'),
				pszDataEmbarque.encode('ascii'),
				pszRGPassageiro.encode('ascii'),
				pszNomePassageiro.encode('ascii'), 
				pszEnderecoPassageiro.encode('ascii')
		 	)

def iCFBPVender_ECF_Daruma(pszCargaTributaria, pszPrecoUnitario, pszTipoDescAcresc, pszValorDescAcresc, pszDescricaoItem):
	return __Biblioteca.iCFBPVender_ECF_Daruma(
				pszCargaTributaria.encode('ascii'),
				pszPrecoUnitario.encode('ascii'),
				pszTipoDescAcresc.encode('ascii'),
				pszValorDescAcresc.encode('ascii'),
				pszDescricaoItem.encode('ascii')
		 	)

		# Cheque
def confCorrigirGeometria_CHEQUE_Daruma(pszNumeroBanco, pszDistValorNumerico, pszColunaValorNumerico, pszDistPrimExtenso, pszColunaPrimExtenso, pszDistSegExtenso, pszColunaSegExtenso, pszDistFavorecido, pszColunaFavorecido, pszDistCidade, pszColunaCidade, pszColunaDia, pszColunaMes, pszColunaAno, pszLinhaAutenticacao, pszColunaAutenticacao):
	return __Biblioteca.confCorrigirGeometria_CHEQUE_Daruma(
				pszNumeroBanco.encode('ascii'),
				pszDistValorNumerico.encode('ascii'),
				pszColunaValorNumerico.encode('ascii'),
				pszDistPrimExtenso.encode('ascii'),
				pszColunaPrimExtenso.encode('ascii'),
				pszDistSegExtenso.encode('ascii'),
				pszColunaSegExtenso.encode('ascii'),
				pszDistFavorecido.encode('ascii'),
				pszColunaFavorecido.encode('ascii'),
				pszDistCidade.encode('ascii'),
				pszColunaCidade.encode('ascii'),
				pszColunaDia.encode('ascii'),
				pszColunaMes.encode('ascii'),
				pszColunaAno.encode('ascii'),
				pszLinhaAutenticacao.encode('ascii'),
				pszColunaAutenticacao.encode('ascii')
		 	)

def iAtributo_CHEQUE_Daruma(pszModo):
	return __Biblioteca.iAtributo_CHEQUE_Daruma(pszModo.encode('ascii'))

def iAutenticar_CHEQUE_Daruma(pszPosicao, pszTexto):
	return __Biblioteca.iAutenticar_CHEQUE_Daruma(pszPosicao.encode('ascii'), pszTexto.encode('ascii'))

def iImprimir_CHEQUE_Daruma(pszNumeroBanco, pszCidade, pszData, pszNomeFavorecido, pszTextoFrente, pszValorCheque):
	return __Biblioteca.iImprimir_CHEQUE_Daruma(
		 		pszNumeroBanco.encode('ascii'),
		 		pszCidade.encode('ascii'),
		 		pszData.encode('ascii'),
		 		pszNomeFavorecido.encode('ascii'),
		 		pszTextoFrente.encode('ascii'),
		 		pszValorCheque.encode('ascii')
		 	)

def iImprimirVerso_CHEQUE_Daruma(pszTexto):
	return __Biblioteca.iImprimirVerso_CHEQUE_Daruma(pszTexto.encode('ascii'))

def iImprimirVertical_CHEQUE_Daruma(pszNumeroBanco, pszCidade, pszData, pszNomeFavorecido, pszTextoFrente, pszValorCheque):
	return __Biblioteca.iImprimirVertical_CHEQUE_Daruma(
		 		pszNumeroBanco.encode('ascii'),
		 		 pszCidade.encode('ascii'),
		 		 pszData.encode('ascii'),
		 		 pszNomeFavorecido.encode('ascii'),
		 		 pszTextoFrente.encode('ascii'),
		 		 pszValorCheque.encode('ascii')
		 	)

def eEjetarCheque_ECF_Daruma():
	return __Biblioteca.eEjetarCheque_ECF_Daruma()

		# Código de barras
def iImprimirCodigoBarras_ECF_Daruma(pszTipo, pszLargura, pszAltura, pszImprTexto, pszCodigo, pszOrientacao, pszTextoLivre):
	return __Biblioteca.iImprimirCodigoBarras_ECF_Daruma(
				pszTipo.encode('ascii'),
				pszLargura.encode('ascii'),
				pszAltura.encode('ascii'),
				pszImprTexto.encode('ascii'),
				pszCodigo.encode('ascii'),
				pszOrientacao.encode('ascii'),
				pszTextoLivre.encode('ascii')
			)

		# Comprovantes de Crédito e Débito CCD
		# Funções TEF - Início
def eTEF_EsperarArquivo_ECF_Daruma(szArquivo, iTempo, bTravarTeclado):
	return __Biblioteca.eTEF_EsperarArquivo_ECF_Daruma(
		 		szArquivo.encode('ascii'),
		 		iTempo,
		 		bTravarTeclado
		 	)

def eTEF_SetarFoco_ECF_Daruma(szNomeTela):
	return __Biblioteca.eTEF_SetarFoco_ECF_Daruma(szNomeTela.encode('ascii'))

def eTEF_TravarTeclado_ECF_Daruma(bTravarTeclado):
	return __Biblioteca.eTEF_TravarTeclado_ECF_Daruma(bTravarTeclado)

def iTEF_ImprimirResposta_ECF_Daruma(szArquivo, bTravarTeclado):
	return __Biblioteca.iTEF_ImprimirResposta_ECF_Daruma(szArquivo.encode('ascii'), bTravarTeclado)

def iTEF_ImprimirRespostaCartao_ECF_Daruma(szArquivo, bTravarTeclado, szForma, szValor):
	return __Biblioteca.iTEF_ImprimirRespostaCartao_ECF_Daruma(
		 		szArquivo.encode('ascii'),
		 		bTravarTeclado,
		 		szForma.encode('ascii'),
		 		szValor.encode('ascii')
		 	)

def iTEF_Fechar_ECF_Daruma():
	return __Biblioteca.iTEF_Fechar_ECF_Daruma()		 	
		# Funções TEF - Fim

def iCCDAbrir_ECF_Daruma(pszFormaPgto, pszParcelas, pszDocOrigem, pszValor, pszCPF, pszNome, pszEndereco):
	return __Biblioteca.iCCDAbrir_ECF_Daruma(
		 		pszFormaPgto.encode('ascii'),
		 		pszParcelas.encode('ascii'),
		 		pszDocOrigem.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszCPF.encode('ascii'),
		 		pszNome.encode('ascii'),
		 		pszEndereco.encode('ascii')
		 	)

def iCCDAbrirPadrao_ECF_Daruma():
	return __Biblioteca.iCCDAbrirPadrao_ECF_Daruma()

def iCCDAbrirSimplificado_ECF_Daruma(pszFormaPgto, pszParcelas, pszDocOrigem, pszValor):
	return __Biblioteca.iCCDAbrirSimplificado_ECF_Daruma(pszFormaPgto,
		 		pszParcelas.encode('ascii'),
		 		pszDocOrigem.encode('ascii'),
		 		pszValor.encode('ascii')
		 	)

def iCCDImprimirTexto_ECF_Daruma(pszTexto):
	return __Biblioteca.iCCDImprimirTexto_ECF_Daruma(pszTexto.encode('ascii'))

def iCCDImprimirArquivo_ECF_Daruma(pszArqOrigem):
	return __Biblioteca.iCCDImprimirArquivo_ECF_Daruma(pszArqOrigem.encode('ascii'))

def iCCDEstornar_ECF_Daruma(pszCOO, pszCPF, pszNome, pszEndereco):
	return __Biblioteca.iCCDEstornar_ECF_Daruma(
		 		pszCOO.encode('ascii'),
		 		 pszCPF.encode('ascii'),
		 		 pszNome.encode('ascii'),
		 		 pszEndereco.encode('ascii')
		 	)

def iCCDEstornarPadrao_ECF_Daruma():
	return __Biblioteca.iCCDEstornarPadrao_ECF_Daruma()

def iCCDFechar_ECF_Daruma():
	return __Biblioteca.iCCDFechar_ECF_Daruma()

def iCCDSegundaVia_ECF_Daruma():
	return __Biblioteca.iCCDSegundaVia_ECF_Daruma()
		
		# Comprovante Não Fiscal
def iCNFAbrir_ECF_Daruma(pszCPF, pszNome, pszEndereco):
	return __Biblioteca.iCNFAbrir_ECF_Daruma(
		 		pszCPF.encode('ascii'),
		 		pszNome.encode('ascii'),
		 		pszEndereco.encode('ascii')
		 	)

def iCNFAbrirPadrao_ECF_Daruma():
	return __Biblioteca.iCNFAbrirPadrao_ECF_Daruma()

def iCNFReceber_ECF_Daruma(pszIndice, pszValor, pszTipoDescAcresc, pszValorDescAcresc):
	return __Biblioteca.iCNFReceber_ECF_Daruma(
		 		pszIndice.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszTipoDescAcresc.encode('ascii'),
		 		pszValorDescAcresc.encode('ascii')
		 	)

def iCNFReceberSemDesc_ECF_Daruma(pszIndice, pszValor):
	return __Biblioteca.iCNFReceberSemDesc_ECF_Daruma(pszIndice.encode('ascii'), pszValor.encode('ascii'))

def iCNFCancelarUltimoItem_ECF_Daruma():
	return __Biblioteca.iCNFCancelarUltimoItem_ECF_Daruma()

def iCNFCancelarItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCNFCancelarItem_ECF_Daruma(pszNumItem.encode('ascii'))

def iCNFCancelarDescontoItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCNFCancelarDescontoItem_ECF_Daruma(pszNumItem.encode('ascii'))

def iCNFCancelarDescontoUltimoItem_ECF_Daruma():
	return __Biblioteca.iCNFCancelarDescontoUltimoItem_ECF_Daruma()

def iCNFCancelarAcrescimoItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCNFCancelarAcrescimoItem_ECF_Daruma(pszNumItem.encode('ascii'))

def iCNFCancelarAcrescimoUltimoItem_ECF_Daruma():
	return __Biblioteca.iCNFCancelarAcrescimoUltimoItem_ECF_Daruma()

def iCNFTotalizarComprovante_ECF_Daruma(pszTipoDescAcresc, pszValorDescAcresc):
	return __Biblioteca.iCNFTotalizarComprovante_ECF_Daruma(pszTipoDescAcresc.encode('ascii'), pszValorDescAcresc.encode('ascii'))

def iCNFTotalizarComprovantePadrao_ECF_Daruma():
	return __Biblioteca.iCNFTotalizarComprovantePadrao_ECF_Daruma()

def iCNFCancelarDescontoSubtotal_ECF_Daruma():
	return __Biblioteca.iCNFCancelarDescontoSubtotal_ECF_Daruma()

def iCNFCancelarAcrescimoSubtotal_ECF_Daruma():
	return __Biblioteca.iCNFCancelarAcrescimoSubtotal_ECF_Daruma()

def iCNFEfetuarPagamento_ECF_Daruma(pszFormaPgto, pszValor, pszInfoAdicional):
	return __Biblioteca.iCNFEfetuarPagamento_ECF_Daruma(
		 		pszFormaPgto.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszInfoAdicional.encode('ascii')
		 	)

def iCNFEfetuarPagamentoFormatado_ECF_Daruma(psszFormaPgto, pszValor):
	return __Biblioteca.iCNFEfetuarPagamentoFormatado_ECF_Daruma(psszFormaPgto.encode('ascii'), pszValor.encode('ascii'))

def iCNFEfetuarPagamentoPadrao_ECF_Daruma():
	return __Biblioteca.iCNFEfetuarPagamentoPadrao_ECF_Daruma()

def iCNFEncerrar_ECF_Daruma(pszMensagem):
	return __Biblioteca.iCNFEncerrar_ECF_Daruma(pszMensagem.encode('ascii'))

def iCNFEncerrarPadrao_ECF_Daruma():
	return __Biblioteca.iCNFEncerrarPadrao_ECF_Daruma()

def iCNFCancelar_ECF_Daruma():
	return __Biblioteca.iCNFCancelar_ECF_Daruma()

		# Configuracoes da Impressora Fiscal
def confCadastrar_ECF_Daruma(pszCadastrar, pszValor, pszSeparador):
	return __Biblioteca.confCadastrar_ECF_Daruma(
		 		pszCadastrar.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszSeparador.encode('ascii')
		 	)

def confCadastrarPadrao_ECF_Daruma(pszCadastrar, pszValor):
	return __Biblioteca.confCadastrarPadrao_ECF_Daruma(pszCadastrar.encode('ascii'), pszValor.encode('ascii'))

def confDesabilitarHorarioVerao_ECF_Daruma():
	return __Biblioteca.confDesabilitarHorarioVerao_ECF_Daruma()

def confDesabilitarModoPreVenda_ECF_Daruma():
	return __Biblioteca.confDesabilitarModoPreVenda_ECF_Daruma()

def confHabilitarHorarioVerao_ECF_Daruma():
	return __Biblioteca.confHabilitarHorarioVerao_ECF_Daruma()

def confHabilitarModoPreVenda_ECF_Daruma():
	return __Biblioteca.confHabilitarModoPreVenda_ECF_Daruma()

def confProgramarAvancoPapel_ECF_Daruma(pszSepEntreLinhas, pszSepEntreDoc, pszLinhasGuilhotina, pszGuilhotina, pszImpClicheAntecipada):
	return __Biblioteca.confProgramarAvancoPapel_ECF_Daruma(
		 		pszSepEntreLinhas.encode('ascii'),
		 		pszSepEntreDoc.encode('ascii'),
		 		pszLinhasGuilhotina.encode('ascii'),
		 		pszGuilhotina.encode('ascii'),
		 		pszImpClicheAntecipada.encode('ascii')
		 	)

def confProgramarIDLoja_ECF_Daruma(pszValor):
	return __Biblioteca.confProgramarIDLoja_ECF_Daruma(pszValor.encode('ascii'))

def confProgramarOperador_ECF_Daruma(pszValor):
	return __Biblioteca.confProgramarOperador_ECF_Daruma(pszValor.encode('ascii'))

		# Cupom Fiscal
def iCFAbrir_ECF_Daruma(pszCPF, pszNome, pszEndereco):
	return __Biblioteca.iCFAbrir_ECF_Daruma(
		 		pszCPF.encode('ascii'), 
		 		pszNome.encode('ascii'), 
		 		pszEndereco.encode('ascii')
		 	)

def iCFAbrirPadrao_ECF_Daruma():
	return __Biblioteca.iCFAbrirPadrao_ECF_Daruma()

def iCFVender_ECF_Daruma(pszCargaTributaria, pszQuantidade, pszPrecoUnitario, pszTipoDescAcresc, pszValorDescAcresc, pszCodigoItem, pszUnidadeMedida, pszDescricaoItem):
	return __Biblioteca.iCFVender_ECF_Daruma(
		 		pszCargaTributaria.encode('ascii'),
		 		pszQuantidade.encode('ascii'),
		 		pszPrecoUnitario.encode('ascii'),
		 		pszTipoDescAcresc.encode('ascii'),
		 		pszValorDescAcresc.encode('ascii'),
		 		pszCodigoItem.encode('ascii'),
		 		pszUnidadeMedida.encode('ascii'),
		 		pszDescricaoItem.encode('ascii')
		 	)

def iCFVenderResumido_ECF_Daruma(pszCargaTributaria, pszPrecoUnitario, pszCodigoItem, pszDescricaoItem):
	return __Biblioteca.iCFVenderResumido_ECF_Daruma(
		 		pszCargaTributaria.encode('ascii'),
		 		pszPrecoUnitario.encode('ascii'),
		 		pszCodigoItem.encode('ascii'),
		 		pszDescricaoItem.encode('ascii')
		 	)

def iCFVenderSemDesc_ECF_Daruma(pszCargaTributaria, pszQuantidade, pszPrecoUnitario, pszCodigoItem, pszUnidadeMedida, pszDescricaoItem):
	return __Biblioteca.iCFVenderSemDesc_ECF_Daruma(
		 		pszCargaTributaria.encode('ascii'),
		 		pszQuantidade.encode('ascii'),
		 		pszPrecoUnitario.encode('ascii'),
		 		pszCodigoItem.encode('ascii'),
		 		pszUnidadeMedida.encode('ascii'),
		 		pszDescricaoItem.encode('ascii')
		 	)

def iCFLancarDescontoItem_ECF_Daruma(pszNumItem, pszTipoDesc, pszValorDesc):
	return __Biblioteca.iCFLancarDescontoItem_ECF_Daruma(
		 		pszNumItem.encode('ascii'),
		 		pszTipoDesc.encode('ascii'),
		 		pszValorDesc.encode('ascii')
		 	)

def iCFLancarAcrescimoItem_ECF_Daruma(pszNumItem, pszTipoAcresc, pszValorAcresc):
	return __Biblioteca.iCFLancarAcrescimoItem_ECF_Daruma(
		 		pszNumItem.encode('ascii'),
		 		pszTipoAcresc.encode('ascii'),
		 		pszValorAcresc.encode('ascii')
		 	)

def iCFLancarDescontoUltimoItem_ECF_Daruma(pszTipoDesc, pszValorDesc):
	return __Biblioteca.iCFLancarDescontoUltimoItem_ECF_Daruma(pszTipoDesc.encode('ascii'), pszValorDesc.encode('ascii'))

def iCFLancarAcrescimoUltimoItem_ECF_Daruma(pszTipoAcresc, pszValorAcresc):
	return __Biblioteca.iCFLancarAcrescimoUltimoItem_ECF_Daruma(pszTipoAcresc.encode('ascii'), pszValorAcresc.encode('ascii'))

def iCFCancelarItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCFCancelarItem_ECF_Daruma(pszNumItem.encode('ascii'))

def iCFCancelarDescontoItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCFCancelarDescontoItem_ECF_Daruma(pszNumItem.encode('ascii'))

def iCFCancelarDescontoUltimoItem_ECF_Daruma():
	return __Biblioteca.iCFCancelarDescontoUltimoItem_ECF_Daruma()

def iCFCancelarAcrescimoItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCFCancelarAcrescimoItem_ECF_Daruma(pszNumItem.encode('ascii'))

def iCFCancelarAcrescimoUltimoItem_ECF_Daruma():
	return __Biblioteca.iCFCancelarAcrescimoUltimoItem_ECF_Daruma()

def iCFCancelarDescontoSubtotal_ECF_Daruma():
	return __Biblioteca.iCFCancelarDescontoSubtotal_ECF_Daruma()

def iCFCancelarAcrescimoSubtotal_ECF_Daruma():
	return __Biblioteca.iCFCancelarAcrescimoSubtotal_ECF_Daruma()

def iCFCancelarItemParcial_ECF_Daruma(pszNumItem, pszQuantidade):
	return __Biblioteca.iCFCancelarItemParcial_ECF_Daruma(pszNumItem.encode('ascii'), pszQuantidade.encode('ascii'))

def iCFCancelarUltimoItem_ECF_Daruma():
	return __Biblioteca.iCFCancelarUltimoItem_ECF_Daruma()

def iCFCancelarUltimoItemParcial_ECF_Daruma(pszQuantidade):
	return __Biblioteca.iCFCancelarUltimoItemParcial_ECF_Daruma(pszQuantidade.encode('ascii'))

def iCFTotalizarCupom_ECF_Daruma(pszTipoDescAcresc, pszValorDescAcresc):
	return __Biblioteca.iCFTotalizarCupom_ECF_Daruma(pszTipoDescAcresc.encode('ascii'), pszValorDescAcresc.encode('ascii'))

def iCFTotalizarCupomPadrao_ECF_Daruma():
	return __Biblioteca.iCFTotalizarCupomPadrao_ECF_Daruma()

def iCFEfetuarPagamento_ECF_Daruma(psszFormaPgto, pszValor, pszInfoAdicional):
	return __Biblioteca.iCFEfetuarPagamento_ECF_Daruma(
		 		psszFormaPgto.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszInfoAdicional.encode('ascii')
		 	)

def iCFEfetuarPagamentoFormatado_ECF_Daruma(pszFormaPgto, pszValor):
	return __Biblioteca.iCFEfetuarPagamentoFormatado_ECF_Daruma(pszFormaPgto.encode('ascii'), pszValor.encode('ascii'))

def iCFEfetuarPagamentoPadrao_ECF_Daruma():
	return __Biblioteca.iCFEfetuarPagamentoPadrao_ECF_Daruma()

def iEstornarPagamento_ECF_Daruma(pszFormaPgtoEstornado, pszFormaPgtoEfetivado, pszValor, pszInfoAdicional):
	return __Biblioteca.iEstornarPagamento_ECF_Daruma(
		 		pszFormaPgtoEstornado.encode('ascii'),
		 		pszFormaPgtoEfetivado.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszInfoAdicional.encode('ascii'))

def iCFIdentificarConsumidor_ECF_Daruma(pszNome, pszEndereco, pszCPF):
	return __Biblioteca.iCFIdentificarConsumidor_ECF_Daruma(
		 		pszNome.encode('ascii'),
		 		pszEndereco.encode('ascii'),
		 		pszCPF.encode('ascii')
		 	)

def iCFEncerrar_ECF_Daruma(pszCupomAdicional, pszMensagem):
	return __Biblioteca.iCFEncerrar_ECF_Daruma(pszCupomAdicional.encode('ascii'), pszMensagem.encode('ascii'))

def iCFEncerrarConfigMsg_ECF_Daruma(pszMensagem):
	return __Biblioteca.iCFEncerrarConfigMsg_ECF_Daruma(pszMensagem.encode('ascii'))

def iCFEncerrarPadrao_ECF_Daruma():
	return __Biblioteca.iCFEncerrarPadrao_ECF_Daruma()

def iCFEncerrarResumido_ECF_Daruma():
	return __Biblioteca.iCFEncerrarResumido_ECF_Daruma()

def iCFCancelar_ECF_Daruma():
	return __Biblioteca.iCFCancelar_ECF_Daruma()

def iCFEmitirCupomAdicional_ECF_Daruma():
	return __Biblioteca.iCFEmitirCupomAdicional_ECF_Daruma()

def rCFSaldoAPagar_ECF_Daruma(pszValor):
	return __Biblioteca.rCFSaldoAPagar_ECF_Daruma(byref(pszValor.encode('ascii')))

def rCFSubTotal_ECF_Daruma(pszValor):
	return __Biblioteca.rCFSubTotal_ECF_Daruma(byref(pszValor.encode('ascii')))

def rCFVerificarStatus_ECF_Daruma(pszStatus, piStatus):
	return __Biblioteca.rCFVerificarStatus_ECF_Daruma(byref(pszStatus.encode('ascii')), byref(piStatus))

def rCMEfetuarCalculo_ECF_Daruma(pszISS, pszICMS):
	return __Biblioteca.rCMEfetuarCalculo_ECF_Daruma(byref(pszISS.encode('ascii')), byref(pszICMS.encode('ascii')))

# Gaveta Autentica Outros
def eAbrirGaveta_ECF_Daruma():
	return __Biblioteca.eAbrirGaveta_ECF_Daruma()

def eAcionarGuilhotina_ECF_Daruma(pszTipoCorte):
	return __Biblioteca.eAcionarGuilhotina_ECF_Daruma(pszTipoCorte.encode('ascii'))

def eCarregarBitmapPromocional_ECF_Daruma(pszPathLogotipo, pszNumBitmap, pszOrientacao):
	return __Biblioteca.eCarregarBitmapPromocional_ECF_Daruma(
		 		pszPathLogotipo.encode('ascii'),
		 		pszNumBitmap.encode('ascii'),
		 		pszOrientacao.encode('ascii')
		 	)

def eSinalSonoro_ECF_Daruma(StrNumeroBeep):
	return __Biblioteca.eSinalSonoro_ECF_Daruma(StrNumeroBeep.encode('ascii'))

def rStatusGaveta_ECF_Daruma(Int_Status):
	return __Biblioteca.rStatusGaveta_ECF_Daruma(byref(Int_Status))

		#Geração de Arquivos
def rGerarEspelhoMFD_ECF_Daruma(pszTipo, pszInicial, pszFinal):
	return __Biblioteca.rGerarEspelhoMFD_ECF_Daruma(
		 		pszTipo.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		pszFinal.encode('ascii')
		 	)

def rGerarRelatorio_ECF_Daruma(szRelatorio, szTipo, pszInicial, pszFinal):
	return __Biblioteca.rGerarRelatorio_ECF_Daruma(
		 		szRelatorio.encode('ascii'),
		 		szTipo.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		pszFinal.encode('ascii')
		 	)

def rGerarRelatorioOffline_ECF_Daruma(szRelatorio, szTipo, pszInicial, pszFinal, szArquivo_MF, szArquivo_MFD, szArquivo_INF):
	return __Biblioteca.rGerarRelatorioOffline_ECF_Daruma(
		 		szRelatorio.encode('ascii'),
		 		szTipo.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		szArquivo_MF.encode('ascii'),
		 		szArquivo_MFD.encode('ascii'),
		 		szArquivo_INF.encode('ascii')
		 	)

def rGerarMapaResumo():
	return __Biblioteca.rGerarMapaResumo()

def rEfetuarDownloadMFD_ECF_Daruma(pszTipo, pszInicial, pszFinal, pszNomeArquivo):
	return __Biblioteca.rEfetuarDownloadMFD_ECF_Daruma(
		 		pszTipo.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		pszFinal.encode('ascii'),
		 		pszNomeArquivo.encode('ascii')
		 	)

def rEfetuarDownloadMF_ECF_Daruma(pszNomeArquivo):
	return __Biblioteca.rEfetuarDownloadMF_ECF_Daruma(pszNomeArquivo.encode('ascii'))

		# Lei DE OLHO no Imposto
def confCFNCM_ECF_Daruma(pszNCM, pszTipoOrigem):
	return __Biblioteca.confCFNCM_ECF_Daruma(pszNCM.encode('ascii'), pszTipoOrigem.encode('ascii'))

def rCFVrImposto_ECF_Daruma(pszNumeroItem, pszVrImposto):
	return __Biblioteca.rCFVrImposto_ECF_Daruma(pszNumeroItem.encode('ascii'), pszVrImposto.encode('ascii'))

		# PAF-ECF
def ePAFCadastrar_ECF_Daruma(pszNomeArquivo, pszChave, pszNumSerieECF, pszGT):
	return __Biblioteca.ePAFCadastrar_ECF_Daruma(
		 		pszNomeArquivo.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszNumSerieECF.encode('ascii'),
		 		pszGT.encode('ascii')
		 	)

def ePAFValidarDados_ECF_Daruma(pszNomeArquivo, pszChave, pszNumSerieEFC, pszGT):
	return __Biblioteca.ePAFValidarDados_ECF_Daruma(
		 		pszNomeArquivo.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszNumSerieEFC.encode('ascii'),
		 		pszGT.encode('ascii')
		 	)

def ePAFAtualizarGT_ECF_Daruma(pszNomeArquivo, pszChave, pszNumSerieECF, pszGT):
	return __Biblioteca.ePAFAtualizarGT_ECF_Daruma(
		 		pszNomeArquivo.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszNumSerieECF.encode('ascii'),
		 		pszGT.encode('ascii')
		 	)

def confModoPAF_ECF_Daruma(pszAtivar, pszChave, pszNomeArquivo):
	return __Biblioteca.confModoPAF_ECF_Daruma(
		 		pszAtivar.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszNomeArquivo.encode('ascii')
		 	)

def rLerArqRegistroPAF_ECF_Daruma(pszCaminho, pszChave, pszReturn):
	return __Biblioteca.rLerArqRegistroPAF_ECF_Daruma(
		 		pszCaminho.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszReturn.encode('ascii')
		 	)

def eRSAAssinarArquivo(szArquivo, szChavePrivada):
	return __Biblioteca.eRSAAssinarArquivo(szArquivo.encode('ascii'), szChavePrivada.encode('ascii'))

def rAssinarRSA_ECF_Daruma(pszPathArquivo, pszChavePrivada, pszAssinaturaGerada):
	return __Biblioteca.rAssinarRSA_ECF_Daruma(
		 		pszPathArquivo.encode('ascii'),
		 		pszChavePrivada.encode('ascii'),
		 		pszAssinaturaGerada.encode('ascii')
		 	)

def rRSAChavePublica(szChavePrivada, szChavePublica, szExpoenteszExpoente):
	return __Biblioteca.rRSAChavePublica(
		 		szChavePrivada.encode('ascii'),
		 		szChavePublica.encode('ascii'),
		 		szExpoenteszExpoente.encode('ascii')
		 	)

def rCalcularMD5_ECF_Daruma(pszPathArquivo, pszMD5GeradoHex, pszMD5GeradoAscii):
	return __Biblioteca.rCalcularMD5_ECF_Daruma(
		 		pszPathArquivo.encode('ascii'),
		 		pszMD5GeradoHex.encode('ascii'),
		 		pszMD5GeradoAscii.encode('ascii')
		 	)

def rCodigoModeloFiscal_ECF_Daruma(pszValor):
	return __Biblioteca.rCodigoModeloFiscal_ECF_Daruma(pszValor.encode('ascii'))

def rRetornarGTCodificado_ECF_Daruma(pszValor):
	return __Biblioteca.rRetornarGTCodificado_ECF_Daruma(pszValor.encode('ascii'))

def rRetornarNumeroSerieCodificado_ECF_Daruma(pszValor):
	return __Biblioteca.rRetornarNumeroSerieCodificado_ECF_Daruma(pszValor.encode('ascii'))

def rVerificarGTCodificado_ECF_Daruma(pszValor):
	return __Biblioteca.rVerificarGTCodificado_ECF_Daruma(pszValor.encode('ascii'))

def rVerificarNumeroSerieCodificado_ECF_Daruma(pszValor):
	return __Biblioteca.rVerificarNumeroSerieCodificado_ECF_Daruma(pszValor.encode('ascii'))

def eMemoriaFiscal_ECF_Daruma(pszInicial, pszFinal, pszCompleta, pszTipo):
	return __Biblioteca.eMemoriaFiscal_ECF_Daruma(
		 		pszInicial.encode('ascii'),
		 		pszFinal.encode('ascii'),
		 		pszCompleta.encode('ascii'),
		 		pszTipo.encode('ascii')
		 	)

		# Registry
def regCFCupomAdicionalDllConfig_ECF_Daruma(pszParametro):
	return __Biblioteca.regCFCupomAdicionalDllConfig_ECF_Daruma(pszParametro.encode('ascii'))

def regSintegra_ECF_Daruma(pszPathChave, pszValor):
	return __Biblioteca.regSintegra_ECF_Daruma(pszPathChave.encode('ascii'), pszValor.encode('ascii'))

		# Relatorio Gerencial
def iRGAbrir_ECF_Daruma(pszNomeRG):
	return __Biblioteca.iRGAbrir_ECF_Daruma(pszNomeRG.encode('ascii'))

def iRGAbrirIndice_ECF_Daruma(pszIndiceRG):
	return __Biblioteca.iRGAbrirIndice_ECF_Daruma(pszIndiceRG)

def iRGAbrirPadrao_ECF_Daruma(pszTexto):
	return __Biblioteca.iRGAbrirPadrao_ECF_Daruma(pszTexto.encode('ascii'))

def iRGImprimirTexto_ECF_Daruma(pszArquivo):
	return __Biblioteca.iRGImprimirTexto_ECF_Daruma(pszArquivo.encode('ascii'))

def iRGImprimirArquivo_ECF_Daruma():
	return __Biblioteca.iRGImprimirArquivo_ECF_Daruma()

def iRGFechar_ECF_Daruma():
	return __Biblioteca.iRGFechar_ECF_Daruma()

def rRGVerificarStatus_ECF_Daruma(pszStatus):
	return __Biblioteca.rRGVerificarStatus_ECF_Daruma(byref(pszStatus.encode('ascii')))

		# Relatorios Fiscais
def iLeituraX_ECF_Daruma():
	return __Biblioteca.iLeituraX_ECF_Daruma()

def rLeituraX_ECF_Daruma():
	return __Biblioteca.rLeituraX_ECF_Daruma()

def rLeituraXCustomizada_ECF_Daruma(pszCaminho):
	return __Biblioteca.rLeituraXCustomizada_ECF_Daruma(pszCaminho.encode('ascii'))

def iMFLer_ECF_Daruma(pszInicial, pszFinal):
	return __Biblioteca.iMFLer_ECF_Daruma(pszInicial.encode('ascii'), pszFinal.encode('ascii'))

def iMFLerSerial_ECF_Daruma(pszInicial, pszFinal):
	return __Biblioteca.iMFLerSerial_ECF_Daruma(pszInicial.encode('ascii'), pszFinal.encode('ascii'))

def iSangria_ECF_Daruma(pszValor, pszMensagem):
	return __Biblioteca.iSangria_ECF_Daruma(pszValor.encode('ascii'), pszMensagem.encode('ascii'))

def iSangriaPadrao_ECF_Daruma():
	return __Biblioteca.iSangriaPadrao_ECF_Daruma()

def iSuprimento_ECF_Daruma(pszValor, pszMensagem):
	return __Biblioteca.iSuprimento_ECF_Daruma(pszValor.encode('ascii'), pszMensagem.encode('ascii'))

def iSuprimentoPadrao_ECF_Daruma():
	return __Biblioteca.iSuprimentoPadrao_ECF_Daruma()

def iRelatorioConfiguracao_ECF_Daruma():
	return __Biblioteca.iRelatorioConfiguracao_ECF_Daruma()

def iReducaoZ_ECF_Daruma(pszData, pszHora):
	return __Biblioteca.iReducaoZ_ECF_Daruma(pszData.encode('ascii'), pszHora.encode('ascii'))

		# Retornos e Status
def eBuscarPortaVelocidade_ECF_Daruma():
	return __Biblioteca.eBuscarPortaVelocidade_ECF_Daruma()

def eRetornarPortasCOM_ECF_Daruma(pszRetorno):
	return __Biblioteca.eRetornarPortasCOM_ECF_Daruma(byref(pszRetorno.encode('ascii')))

def eInterpretarRetorno_ECF_Daruma(iIndice, pszRetorno):
	return __Biblioteca.eInterpretarRetorno_ECF_Daruma(iIndice, pszRetorno.encode('ascii'))

def eInterpretarAviso_ECF_Daruma(iIndice, pszRetorno):
	return __Biblioteca.eInterpretarAviso_ECF_Daruma(iIndice, pszRetorno.encode('ascii'))

def eInterpretarErro_ECF_Daruma(iIndice, pszRetorno):
	return __Biblioteca.eInterpretarErro_ECF_Daruma(iIndice, pszRetorno.encode('ascii'))

def eRetornarAvisoErroUltimoCMD_ECF_Daruma(Str_Aviso, Str_Erro):
	return __Biblioteca.eRetornarAvisoErroUltimoCMD_ECF_Daruma(Str_Aviso.encode('ascii'), Str_Erro.encode('ascii'))

def rStatusImpressora_ECF_Daruma(pszStatus):
	return __Biblioteca.rStatusImpressora_ECF_Daruma(byref(pszStatus.encode('ascii')))

def rStatusImpressoraBinario_ECF_Daruma(pszStatus):
	return __Biblioteca.rStatusImpressoraBinario_ECF_Daruma(byref(pszStatus.encode('ascii')))

def rConsultaStatusImpressoraInt_ECF_Daruma(iIndice, iRetorno):
	return __Biblioteca.rConsultaStatusImpressoraInt_ECF_Daruma(iIndice, byref(iRetorno))

def rConsultaStatusImpressoraStr_ECF_Daruma(iIndice, szStatus):
	return __Biblioteca.rConsultaStatusImpressoraStr_ECF_Daruma(iIndice, byref(szStatus))

def rStatusUltimoCmd_ECF_Daruma(pszErro, pszAviso, piErro, piAviso):
	return __Biblioteca.rStatusUltimoCmd_ECF_Daruma(
		 		byref(pszErro.encode('ascii')),
		 		byref(pszAviso.encode('ascii')),
		 		byref(piErro),
		 		byref(piAviso))

def rStatusUltimoCMDInt_ECF_Daruma(iErro, iAviso):
	return __Biblioteca.rStatusUltimoCMDInt_ECF_Daruma(byref(iErro), byref(iAviso))

def rStatusUltimoCmdStr_ECF_Daruma(pszErro, pszAviso):
	return __Biblioteca.rStatusUltimoCmdStr_ECF_Daruma(byref(pszErro.encode('ascii')), byref(pszAviso.encode('ascii')))

def rInfoEstendida_ECF_Daruma(indice, pszRetorno):
	return __Biblioteca.rInfoEstendida_ECF_Daruma(indice, byref(pszRetorno.encode('ascii')))

def rInfoEstendida1_ECF_Daruma(pszInfo1):
	return __Biblioteca.rInfoEstendida1_ECF_Daruma(byref(pszInfo1.encode('ascii')))

def rInfoEstendida2_ECF_Daruma(pszInfo2):
	return __Biblioteca.rInfoEstendida2_ECF_Daruma(byref(pszInfo2.encode('ascii')))

def rInfoEstendida3_ECF_Daruma(pszInfo3):
	return __Biblioteca.rInfoEstendida3_ECF_Daruma(byref(pszInfo3.encode('ascii')))

def rInfoEstendida4_ECF_Daruma(pszInfo4):
	return __Biblioteca.rInfoEstendida4_ECF_Daruma(byref(pszInfo4.encode('ascii')))

def rInfoEstendida5_ECF_Daruma(pszInfo5):
	return __Biblioteca.rInfoEstendida5_ECF_Daruma(byref(pszInfo5.encode('ascii')))

def rRetornarInformacao_ECF_Daruma(pszIndice, pszRetornar):
	return __Biblioteca.rRetornarInformacao_ECF_Daruma(pszIndice.encode('ascii'), byref(pszRetornar.encode('ascii')))

def rRetornarInformacaoSeparador_ECF_Daruma(pszIndice, pszVSignificativo, pszRetornar):
	return __Biblioteca.rRetornarInformacaoSeparador_ECF_Daruma(
		 		pszIndice.encode('ascii'), 
		 		pszVSignificativo.encode('ascii'), 
		 		byref(pszRetornar.encode('ascii')
		 	))

def rLerAliquotas_ECF_Daruma(cAliquotas):
	return __Biblioteca.rLerAliquotas_ECF_Daruma(byref(cAliquotas.encode('ascii')))

def rLerMeiosPagto_ECF_Daruma(pszRelatorios):
	return __Biblioteca.rLerMeiosPagto_ECF_Daruma(byref(pszRelatorios.encode('ascii')))

def rLerRG_ECF_Daruma(pszRelatorios):
	return __Biblioteca.rLerRG_ECF_Daruma(byref(pszRelatorios.encode('ascii')))

def rLerCNF_ECF_Daruma(pszTotalizadores):
	return __Biblioteca.rLerCNF_ECF_Daruma(byref(pszTotalizadores.encode('ascii')))

def rInfoCNF_ECF_Daruma(pszRetorno):
	return __Biblioteca.rInfoCNF_ECF_Daruma(byref(pszRetorno.encode('ascii')))

def rLerDecimais_ECF_Daruma(pszDecimalQtde, pszDecimalValor, piDecimalQtde, piDecimalValor):
	return __Biblioteca.rLerDecimais_ECF_Daruma(
		 		byref(pszDecimalQtde.encode('ascii')),
		 		byref(pszDecimalValor.encode('ascii')),
		 		byref(piDecimalQtde),
		 		byref(piDecimalValor)
		 	)

def rLerDecimaisInt_ECF_Daruma(piDecimalQtde, piDecimalValor):
	return __Biblioteca.rLerDecimaisInt_ECF_Daruma(byref(piDecimalQtde), byref(piDecimalValor))

def rLerDecimaisStr_ECF_Daruma(pszDecimalQtde, pszDecimalValor):
	return __Biblioteca.rLerDecimaisStr_ECF_Daruma(byref(piDecimalQtde.encode('ascii')), byref(piDecimalValor.encode('ascii')))

def rCompararDataHora_ECF_Daruma(iDiferenca):
	return __Biblioteca.rCompararDataHora_ECF_Daruma(byref(iDiferenca))

def rDataHoraImpressora_ECF_Daruma(pszData, pszHora):
	return __Biblioteca.rDataHoraImpressora_ECF_Daruma(byref(pszData.encode('ascii')), byref(pszHora.encode('ascii')))

def rVerificarImpressoraLigada_ECF_Daruma():
	return __Biblioteca.rVerificarImpressoraLigada_ECF_Daruma()

def rVerificarReducaoZ_ECF_Daruma(pszPendente):
	return __Biblioteca.rVerificarReducaoZ_ECF_Daruma(byref(pszPendente.encode('ascii')))

def rRetornarDadosReducaoZ_ECF_Daruma(pszRetorno):
	return __Biblioteca.rRetornarDadosReducaoZ_ECF_Daruma(byref(pszRetorno.encode('ascii')))

def rTipoUltimoDocumentoInt_ECF_Daruma(iDoc):
	return __Biblioteca.rTipoUltimoDocumentoInt_ECF_Daruma(byref(iDoc))

def rTipoUltimoDocumentoStr_ECF_Daruma(pszDoc):
	return __Biblioteca.rTipoUltimoDocumentoStr_ECF_Daruma(byref(pszDoc.encode('ascii')))

def rUltimoCMDEnviado_ECF_Daruma(pszComando):
	return __Biblioteca.rUltimoCMDEnviado_ECF_Daruma(byref(pszComando.encode('ascii')))

def rMinasLegal_ECF_Daruma(pszRetorno):
	return __Biblioteca.rMinasLegal_ECF_Daruma(byref(pszRetorno.encode('ascii')))

def rRetornarVendaBruta_ECF_Daruma(pszRetorno):
	return __Biblioteca.rRetornarVendaBruta_ECF_Daruma(byref(pszRetorno.encode('ascii')))

def rRetornarVendaLiquida_ECF_Daruma(pszVendaLiquida):
	return __Biblioteca.rRetornarVendaLiquida_ECF_Daruma(byref(pszVendaLiquida.encode('ascii')))

def rCFSaldoAPagar_ECF_Daruma(pszValor):
	return __Biblioteca.rCFSaldoAPagar_ECF_Daruma(byref(pszValor.encode('ascii')))

def rCFSubTotal_ECF_Daruma(pszValor):
	return __Biblioteca.rCFSubTotal_ECF_Daruma(byref(pszValor.encode('ascii')))

		# WebService
def eWsEnviarCupom_ECF_Daruma(pszCPF, pszNomeFantasia, pszIndiceSegmento, pszCCF, pszData, pszHora, pszValor, pszISS, pszICMS, szReservado, iRespostaWS):
	return __Biblioteca.eWsEnviarCupom_ECF_Daruma(
		 		pszCPF.encode('ascii'),
		 		pszNomeFantasia.encode('ascii'),
		 		pszIndiceSegmento.encode('ascii'),
		 		pszCCF.encode('ascii'),
		 		pszData.encode('ascii'),
		 		pszHora.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszISS.encode('ascii'),
		 		pszICMS.encode('ascii'),
		 		szReservado,
		 		byref(iRespostaWS))

def eWsStatus_ECF_Daruma(iRespostaWS):
	return __Biblioteca.eWsStatus_ECF_Daruma(byref(iRespostaWS))

def regAguardarProcesso_DUAL_DarumaFramework(valor):
	return __Biblioteca.regAguardarProcesso_DUAL_DarumaFramework()

def regCodePageAutomatico_DUAL_DarumaFramework(valor):
	return __Biblioteca.regCodePageAutomatico_DUAL_DarumaFramework()

def regEnterFinal_DUAL_DarumaFramework(valor):
	return __Biblioteca.regEnterFinal_DUAL_DarumaFramework()

def regInicializou_DUAL_DarumaFramework(valor):
	return __Biblioteca.regInicializou_DUAL_DarumaFramework()

def regLinhasGuilhotina_DUAL_DarumaFramework(valor):
	return __Biblioteca.regLinhasGuilhotina_DUAL_DarumaFramework()

def regModoGaveta_DUAL_DarumaFramework(gavetastatus):
	return __Biblioteca.regModoGaveta_DUAL_DarumaFramework()

def regPortaComunicacao_DUAL_DarumaFramework(valor):
	return __Biblioteca.regPortaComunicacao_DUAL_DarumaFramework()

def regTabulacao_DUAL_DarumaFramework(valor):
	return __Biblioteca.regTabulacao_DUAL_DarumaFramework()

def regTermica_DUAL_DarumaFramework(valor):
	return __Biblioteca.regTermica_DUAL_DarumaFramework()

def regVelocidade_DUAL_DarumaFramework(valor):
	return __Biblioteca.regVelocidade_DUAL_DarumaFramework()

def regZeroCortado_DUAL_DarumaFramework(valor):
	return __Biblioteca.regZeroCortado_DUAL_DarumaFramework()

def rConsultaStatusImpressora_DUAL_DarumaFramework(indice, tipo, impressoraStatus):
	return __Biblioteca.rConsultaStatusImpressora_DUAL_DarumaFramework()

def rStatusDocumento_DUAL_DarumaFramework(void):
	return __Biblioteca.rStatusDocumento_DUAL_DarumaFramework()

def rStatusGaveta_DUAL_DarumaFramework(gavetaStatus):
	return __Biblioteca.rStatusGaveta_DUAL_DarumaFramework()

def rStatusImpressora_DUAL_DarumaFramework(void):
	return __Biblioteca.rStatusImpressora_DUAL_DarumaFramework()

def rStatusGuilhotina_DUAL_DarumaFramework(void):
	return __Biblioteca.rStatusGuilhotina_DUAL_DarumaFramework()

def iAcionarGaveta_DUAL_DarumaFramework(void):
	return __Biblioteca.iAcionarGaveta_DUAL_DarumaFramework()

def iAutenticarDocumento_DUAL_DarumaFramework(documento, local, timeout):
	return __Biblioteca.iAutenticarDocumento_DUAL_DarumaFramework()

def iImprimirArquivo_DUAL_DarumaFramework(arquivo):
	return __Biblioteca.iImprimirArquivo_DUAL_DarumaFramework()

def iImprimirTexto_DUAL_DarumaFramework(texto, tamanhoTexto):
	return __Biblioteca.iImprimirTexto_DUAL_DarumaFramework()

def iConfigurarGuilhotina_DUAL_DarumaFramework(habilitar, quantidadeLinha):
	return __Biblioteca.iConfigurarGuilhotina_DUAL_DarumaFramework()

def iEnviarBMP_DUAL_DarumaFramework(arquivoOrigem):
	return __Biblioteca.iEnviarBMP_DUAL_DarumaFramework()

def iLimparBuffer_DUAL_DarumaFramework(void):
	return __Biblioteca.iLimparBuffer_DUAL_DarumaFramework()

def iReinicializar_DUAL_DarumaFramework(void):
	return __Biblioteca.iReinicializar_DUAL_DarumaFramework()

def eAtivarConexaoCsd_MODEM_DarumaFramework():
	return __Biblioteca.eAtivarConexaoCsd_MODEM_DarumaFramework()

def eApagarSms_MODEM_DarumaFramework(indice):
	return __Biblioteca.eApagarSms_MODEM_DarumaFramework()

def eFinalizarChamadaCsd_MODEM_DarumaFramework():
	return __Biblioteca.eFinalizarChamadaCsd_MODEM_DarumaFramework()

def eReiniciar_MODEM_DarumaFramework():
	return __Biblioteca.eReiniciar_MODEM_DarumaFramework()

def eInicializar_MODEM_DarumaFramework():
	return __Biblioteca.eInicializar_MODEM_DarumaFramework()

def eRealizarChamadaCsd_MODEM_DarumaFramework(telefone):
	return __Biblioteca.eRealizarChamadaCsd_MODEM_DarumaFramework()

def eTrocarBandeja_MODEM_DarumaFramework():
	return __Biblioteca.eTrocarBandeja_MODEM_DarumaFramework()

def regLerApagar_MODEM_DarumaFramework(valor):
	return __Biblioteca.regLerApagar_MODEM_DarumaFramework()

def regPorta_MODEM_DarumaFramework(valor):
	return __Biblioteca.regPorta_MODEM_DarumaFramework()

def regThread_MODEM_DarumaFramework(valor):
	return __Biblioteca.regThread_MODEM_DarumaFramework()

def regVelocidade_MODEM_DarumaFramework(valor):
	return __Biblioteca.regVelocidade_MODEM_DarumaFramework()

def regCaptionWinAPP_MODEM_DarumaFramework(valor):
	return __Biblioteca.regCaptionWinAPP_MODEM_DarumaFramework()

def regBandejaInicio_MODEM_DarumaFramework(valor):
	return __Biblioteca.regBandejaInicio_MODEM_DarumaFramework()

def regTempoAlertar_MODEM_DarumaFramework(valor):
	return __Biblioteca.regTempoAlertar_MODEM_DarumaFramework()

def rReceberSms_MODEM_DarumaFramework(indice, mensagem, data, hora, remetente):
	return __Biblioteca.rReceberSms_MODEM_DarumaFramework()

def rReceberSmsIndice_MODEM_DarumaFramework(indice, mensagem, data, hora, remetente):
	return __Biblioteca.rReceberSmsIndice_MODEM_DarumaFramework()

def rRetornarImei_MODEM_DarumaFramework(imei):
	return __Biblioteca.rRetornarImei_MODEM_DarumaFramework()

def rRetornarOperadora_MODEM_DarumaFramework(operadora):
	return __Biblioteca.rRetornarOperadora_MODEM_DarumaFramework()

def rReceberDadosCsd_MODEM_DarumaFramework(resposta):
	return __Biblioteca.rReceberDadosCsd_MODEM_DarumaFramework()

def rNivelSinalRecebido_MODEM_DarumaFramework():
	return __Biblioteca.rNivelSinalRecebido_MODEM_DarumaFramework()

def rListarSms_MODEM_DarumaFramework():
	return __Biblioteca.rListarSms_MODEM_DarumaFramework()

def tEnviarDadosCsd_MODEM_DarumaFramework(dados):
	return __Biblioteca.tEnviarDadosCsd_MODEM_DarumaFramework()

def tEnviarSms_MODEM_DarumaFramework(telefone, mensagem):
	return __Biblioteca.tEnviarSms_MODEM_DarumaFramework()

def tEnviarSmsOperadora_MODEM_DarumaFramework(telefone, bandeja, mensagem):
	return __Biblioteca.tEnviarSmsOperadora_MODEM_DarumaFramework()

def eBuscarPortaVelocide_MODEM_DarumaFramework():
	return __Biblioteca.eBuscarPortaVelocide_MODEM_DarumaFramework()