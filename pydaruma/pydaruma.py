from ctypes import *
import platform


if platform.system() == 'Windows':
	__NomeBiblioteca = 'DarumaFrameWork'
	__ExtBiblioteca = '.dll'
	__PathBiblioteca = ''
	#__Biblioteca = windll.LoadLibrary(__PathBiblioteca + __NomeBiblioteca + __ExtBiblioteca)
	__Biblioteca = windll.__getattr__(__PathBiblioteca + __NomeBiblioteca + __ExtBiblioteca)
else:
	__NomeBiblioteca = 'libDarumaFramework'
	__ExtBiblioteca = '.so'
	__PathBiblioteca = '/usr/local/lib/'
	__Biblioteca = CDLL.LoadLibrary(__PathBiblioteca + __NomeBiblioteca + __ExtBiblioteca)

''' Métodos do modulo geral '''
def eDefinirProduto_Daruma(pszProduto):
	return __Biblioteca.eDefinirProduto_Daruma(pszProduto.encode('latin-1'))

''' Métodos do modulo registry '''
def regRetornaValorChave_DarumaFramework(pszProduto, pszChave, pszValor):
	return __Biblioteca.regRetornaValorChave_DarumaFramework(
		pszProduto.encode('latin-1'), 
		pszChave.encode('latin-1'), 
		byref(c_char_p(bytes(pszValor)))
	)

def regAlterarValor_Daruma(pszPathChave, pszValor):
	return __Biblioteca.regAlterarValor_Daruma(
		pszPathChave.encode('latin-1'),
		pszValor.encode('latin-1')
	)

''' Métodos do modulo genérico '''
def eAbrirSerial_Daruma(StrPorta, StrVelocidade):
	return __Biblioteca.eAbrirSerial_Daruma(StrPorta.encode('latin-1'), StrVelocidade.encode('latin-1'))

def eFecharSerial_Daruma():
	return __Biblioteca.eFecharSerial_Daruma()

def tEnviarDados_Daruma(StrInformacao, iTamanhoBytes):
	return __Biblioteca.tEnviarDados_Daruma(StrInformacao.encode('latin-1'), iTamanhoBytes)

def rReceberDados_Daruma(StrInformacao):
	return __Biblioteca.rReceberDados_Daruma(c_char_p(StrInformacao))

'''
Métodos do modulo ECF
Bilhete de passagem
'''
def confCFBPProgramarUF_ECF_Daruma(pszUF):
	return __Biblioteca.confCFBPProgramarUF_ECF_Daruma(pszUF.encode('latin-1'))

def iCFBPAbrir_ECF_Daruma(pszOrigem, pszDestino, pszUFDestino, pszPercurso, pszPrestadora, pszPlataforma, pszPoltrona, pszModalidadetransp, pszCategoriaTransp, pszDataEmbarque, pszRGPassageiro, pszNomePassageiro, pszEnderecoPassageiro):
	return __Biblioteca.iCFBPAbrir_ECF_Daruma(
		pszOrigem.encode('latin-1'),
		pszDestino.encode('latin-1'),
		pszUFDestino.encode('latin-1'),
		pszPercurso.encode('latin-1'),
		pszPrestadora.encode('latin-1'),
		pszPlataforma.encode('latin-1'),
		pszPoltrona.encode('latin-1'),
		pszModalidadetransp.encode('latin-1'),
		pszCategoriaTransp.encode('latin-1'),
		pszDataEmbarque.encode('latin-1'),
		pszRGPassageiro.encode('latin-1'),
		pszNomePassageiro.encode('latin-1'), 
		pszEnderecoPassageiro.encode('latin-1')
	)

def iCFBPVender_ECF_Daruma(pszCargaTributaria, pszPrecoUnitario, pszTipoDescAcresc, pszValorDescAcresc, pszDescricaoItem):
	return __Biblioteca.iCFBPVender_ECF_Daruma(
		pszCargaTributaria.encode('latin-1'),
		pszPrecoUnitario.encode('latin-1'),
		pszTipoDescAcresc.encode('latin-1'),
		pszValorDescAcresc.encode('latin-1'),
		pszDescricaoItem.encode('latin-1')
	)

''' Cheque '''
def confCorrigirGeometria_CHEQUE_Daruma(pszNumeroBanco, pszDistValorNumerico, pszColunaValorNumerico, pszDistPrimExtenso, pszColunaPrimExtenso, pszDistSegExtenso, pszColunaSegExtenso, pszDistFavorecido, pszColunaFavorecido, pszDistCidade, pszColunaCidade, pszColunaDia, pszColunaMes, pszColunaAno, pszLinhaAutenticacao, pszColunaAutenticacao):
	return __Biblioteca.confCorrigirGeometria_CHEQUE_Daruma(
		pszNumeroBanco.encode('latin-1'),
		pszDistValorNumerico.encode('latin-1'),
		pszColunaValorNumerico.encode('latin-1'),
		pszDistPrimExtenso.encode('latin-1'),
		pszColunaPrimExtenso.encode('latin-1'),
		pszDistSegExtenso.encode('latin-1'),
		pszColunaSegExtenso.encode('latin-1'),
		pszDistFavorecido.encode('latin-1'),
		pszColunaFavorecido.encode('latin-1'),
		pszDistCidade.encode('latin-1'),
		pszColunaCidade.encode('latin-1'),
		pszColunaDia.encode('latin-1'),
		pszColunaMes.encode('latin-1'),
		pszColunaAno.encode('latin-1'),
		pszLinhaAutenticacao.encode('latin-1'),
		pszColunaAutenticacao.encode('latin-1')
	)

def iAtributo_CHEQUE_Daruma(pszModo):
	return __Biblioteca.iAtributo_CHEQUE_Daruma(pszModo.encode('latin-1'))

def iAutenticar_CHEQUE_Daruma(pszPosicao, pszTexto):
	return __Biblioteca.iAutenticar_CHEQUE_Daruma(pszPosicao.encode('latin-1'), pszTexto.encode('latin-1'))

def iImprimir_CHEQUE_Daruma(pszNumeroBanco, pszCidade, pszData, pszNomeFavorecido, pszTextoFrente, pszValorCheque):
	return __Biblioteca.iImprimir_CHEQUE_Daruma(
		pszNumeroBanco.encode('latin-1'),
		pszCidade.encode('latin-1'),
		pszData.encode('latin-1'),
		pszNomeFavorecido.encode('latin-1'),
		pszTextoFrente.encode('latin-1'),
		pszValorCheque.encode('latin-1')
	)

def iImprimirVerso_CHEQUE_Daruma(pszTexto):
	return __Biblioteca.iImprimirVerso_CHEQUE_Daruma(pszTexto.encode('latin-1'))

def iImprimirVertical_CHEQUE_Daruma(pszNumeroBanco, pszCidade, pszData, pszNomeFavorecido, pszTextoFrente, pszValorCheque):
	return __Biblioteca.iImprimirVertical_CHEQUE_Daruma(
		pszNumeroBanco.encode('latin-1'),
		pszCidade.encode('latin-1'),
		pszData.encode('latin-1'),
		pszNomeFavorecido.encode('latin-1'),
		pszTextoFrente.encode('latin-1'),
		pszValorCheque.encode('latin-1')
	)

def eEjetarCheque_ECF_Daruma():
	return __Biblioteca.eEjetarCheque_ECF_Daruma()

''' Código de barras '''
def iImprimirCodigoBarras_ECF_Daruma(pszTipo, pszLargura, pszAltura, pszImprTexto, pszCodigo, pszOrientacao, pszTextoLivre):
	return __Biblioteca.iImprimirCodigoBarras_ECF_Daruma(
		pszTipo.encode('latin-1'),
		pszLargura.encode('latin-1'),
		pszAltura.encode('latin-1'),
		pszImprTexto.encode('latin-1'),
		pszCodigo.encode('latin-1'),
		pszOrientacao.encode('latin-1'),
		pszTextoLivre.encode('latin-1')
	)

'''
Comprovantes de Crédito e Débito CCD
Funções TEF - Início
'''
def eTEF_EsperarArquivo_ECF_Daruma(szArquivo, iTempo, bTravarTeclado):
	return __Biblioteca.eTEF_EsperarArquivo_ECF_Daruma(
		szArquivo.encode('latin-1'),
		iTempo,
		bTravarTeclado
	)

def eTEF_SetarFoco_ECF_Daruma(szNomeTela):
	return __Biblioteca.eTEF_SetarFoco_ECF_Daruma(szNomeTela.encode('latin-1'))

def eTEF_TravarTeclado_ECF_Daruma(bTravarTeclado):
	return __Biblioteca.eTEF_TravarTeclado_ECF_Daruma(bTravarTeclado)

def iTEF_ImprimirResposta_ECF_Daruma(szArquivo, bTravarTeclado):
	return __Biblioteca.iTEF_ImprimirResposta_ECF_Daruma(szArquivo.encode('latin-1'), bTravarTeclado)

def iTEF_ImprimirRespostaCartao_ECF_Daruma(szArquivo, bTravarTeclado, szForma, szValor):
	return __Biblioteca.iTEF_ImprimirRespostaCartao_ECF_Daruma(
		szArquivo.encode('latin-1'),
		bTravarTeclado,
		szForma.encode('latin-1'),
		szValor.encode('latin-1')
	)

def iTEF_Fechar_ECF_Daruma():
	return __Biblioteca.iTEF_Fechar_ECF_Daruma()		 	
''' Funções TEF - Fim '''

def iCCDAbrir_ECF_Daruma(pszFormaPgto, pszParcelas, pszDocOrigem, pszValor, pszCPF, pszNome, pszEndereco):
	return __Biblioteca.iCCDAbrir_ECF_Daruma(
		pszFormaPgto.encode('latin-1'),
		pszParcelas.encode('latin-1'),
		pszDocOrigem.encode('latin-1'),
		pszValor.encode('latin-1'),
		pszCPF.encode('latin-1'),
		pszNome.encode('latin-1'),
		pszEndereco.encode('latin-1')
	)

def iCCDAbrirPadrao_ECF_Daruma():
	return __Biblioteca.iCCDAbrirPadrao_ECF_Daruma()

def iCCDAbrirSimplificado_ECF_Daruma(pszFormaPgto, pszParcelas, pszDocOrigem, pszValor):
	return __Biblioteca.iCCDAbrirSimplificado_ECF_Daruma(
		pszFormaPgto.encode('latin-1'),
		pszParcelas.encode('latin-1'),
		pszDocOrigem.encode('latin-1'),
		pszValor.encode('latin-1')
	)

def iCCDImprimirTexto_ECF_Daruma(pszTexto):
	return __Biblioteca.iCCDImprimirTexto_ECF_Daruma(pszTexto.encode('latin-1'))

def iCCDImprimirArquivo_ECF_Daruma(pszArqOrigem):
	return __Biblioteca.iCCDImprimirArquivo_ECF_Daruma(pszArqOrigem.encode('latin-1'))

def iCCDEstornar_ECF_Daruma(pszCOO, pszCPF, pszNome, pszEndereco):
	return __Biblioteca.iCCDEstornar_ECF_Daruma(
		pszCOO.encode('latin-1'),
		pszCPF.encode('latin-1'),
		pszNome.encode('latin-1'),
		pszEndereco.encode('latin-1')
	)

def iCCDEstornarPadrao_ECF_Daruma():
	return __Biblioteca.iCCDEstornarPadrao_ECF_Daruma()

def iCCDFechar_ECF_Daruma():
	return __Biblioteca.iCCDFechar_ECF_Daruma()

def iCCDSegundaVia_ECF_Daruma():
	return __Biblioteca.iCCDSegundaVia_ECF_Daruma()
		
''' Comprovante Não Fiscal '''
def iCNFAbrir_ECF_Daruma(pszCPF, pszNome, pszEndereco):
	return __Biblioteca.iCNFAbrir_ECF_Daruma(
		pszCPF.encode('latin-1'),
		pszNome.encode('latin-1'),
		pszEndereco.encode('latin-1')
	)

def iCNFAbrirPadrao_ECF_Daruma():
	return __Biblioteca.iCNFAbrirPadrao_ECF_Daruma()

def iCNFReceber_ECF_Daruma(pszIndice, pszValor, pszTipoDescAcresc, pszValorDescAcresc):
	return __Biblioteca.iCNFReceber_ECF_Daruma(
		pszIndice.encode('latin-1'),
		pszValor.encode('latin-1'),
		pszTipoDescAcresc.encode('latin-1'),
		pszValorDescAcresc.encode('latin-1')
	)

def iCNFReceberSemDesc_ECF_Daruma(pszIndice, pszValor):
	return __Biblioteca.iCNFReceberSemDesc_ECF_Daruma(pszIndice.encode('latin-1'), pszValor.encode('latin-1'))

def iCNFCancelarUltimoItem_ECF_Daruma():
	return __Biblioteca.iCNFCancelarUltimoItem_ECF_Daruma()

def iCNFCancelarItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCNFCancelarItem_ECF_Daruma(pszNumItem.encode('latin-1'))

def iCNFCancelarDescontoItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCNFCancelarDescontoItem_ECF_Daruma(pszNumItem.encode('latin-1'))

def iCNFCancelarDescontoUltimoItem_ECF_Daruma():
	return __Biblioteca.iCNFCancelarDescontoUltimoItem_ECF_Daruma()

def iCNFCancelarAcrescimoItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCNFCancelarAcrescimoItem_ECF_Daruma(pszNumItem.encode('latin-1'))

def iCNFCancelarAcrescimoUltimoItem_ECF_Daruma():
	return __Biblioteca.iCNFCancelarAcrescimoUltimoItem_ECF_Daruma()

def iCNFTotalizarComprovante_ECF_Daruma(pszTipoDescAcresc, pszValorDescAcresc):
	return __Biblioteca.iCNFTotalizarComprovante_ECF_Daruma(pszTipoDescAcresc.encode('latin-1'), pszValorDescAcresc.encode('latin-1'))

def iCNFTotalizarComprovantePadrao_ECF_Daruma():
	return __Biblioteca.iCNFTotalizarComprovantePadrao_ECF_Daruma()

def iCNFCancelarDescontoSubtotal_ECF_Daruma():
	return __Biblioteca.iCNFCancelarDescontoSubtotal_ECF_Daruma()

def iCNFCancelarAcrescimoSubtotal_ECF_Daruma():
	return __Biblioteca.iCNFCancelarAcrescimoSubtotal_ECF_Daruma()

def iCNFEfetuarPagamento_ECF_Daruma(pszFormaPgto, pszValor, pszInfoAdicional):
	return __Biblioteca.iCNFEfetuarPagamento_ECF_Daruma(
		pszFormaPgto.encode('latin-1'),
		pszValor.encode('latin-1'),
		pszInfoAdicional.encode('latin-1')
	)

def iCNFEfetuarPagamentoFormatado_ECF_Daruma(psszFormaPgto, pszValor):
	return __Biblioteca.iCNFEfetuarPagamentoFormatado_ECF_Daruma(psszFormaPgto.encode('latin-1'), pszValor.encode('latin-1'))

def iCNFEfetuarPagamentoPadrao_ECF_Daruma():
	return __Biblioteca.iCNFEfetuarPagamentoPadrao_ECF_Daruma()

def iCNFEncerrar_ECF_Daruma(pszMensagem):
	return __Biblioteca.iCNFEncerrar_ECF_Daruma(pszMensagem.encode('latin-1'))

def iCNFEncerrarPadrao_ECF_Daruma():
	return __Biblioteca.iCNFEncerrarPadrao_ECF_Daruma()

def iCNFCancelar_ECF_Daruma():
	return __Biblioteca.iCNFCancelar_ECF_Daruma()

''' Configuracoes da Impressora Fiscal '''
def confCadastrar_ECF_Daruma(pszCadastrar, pszValor, pszSeparador):
	return __Biblioteca.confCadastrar_ECF_Daruma(
		pszCadastrar.encode('latin-1'),
		pszValor.encode('latin-1'),
		pszSeparador.encode('latin-1')
	)

def confCadastrarPadrao_ECF_Daruma(pszCadastrar, pszValor):
	return __Biblioteca.confCadastrarPadrao_ECF_Daruma(pszCadastrar.encode('latin-1'), pszValor.encode('latin-1'))

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
		pszSepEntreLinhas.encode('latin-1'),
		pszSepEntreDoc.encode('latin-1'),
		pszLinhasGuilhotina.encode('latin-1'),
		pszGuilhotina.encode('latin-1'),
		pszImpClicheAntecipada.encode('latin-1')
	)

def confProgramarIDLoja_ECF_Daruma(pszValor):
	return __Biblioteca.confProgramarIDLoja_ECF_Daruma(pszValor.encode('latin-1'))

def confProgramarOperador_ECF_Daruma(pszValor):
	return __Biblioteca.confProgramarOperador_ECF_Daruma(pszValor.encode('latin-1'))

''' Cupom Fiscal '''
def iCFAbrir_ECF_Daruma(pszCPF, pszNome, pszEndereco):
	return __Biblioteca.iCFAbrir_ECF_Daruma(
		pszCPF.encode('latin-1'), 
		pszNome.encode('latin-1'), 
		pszEndereco.encode('latin-1')
	)

def iCFAbrirPadrao_ECF_Daruma():
	return __Biblioteca.iCFAbrirPadrao_ECF_Daruma()

def iCFVender_ECF_Daruma(pszCargaTributaria, pszQuantidade, pszPrecoUnitario, pszTipoDescAcresc, pszValorDescAcresc, pszCodigoItem, pszUnidadeMedida, pszDescricaoItem):
	return __Biblioteca.iCFVender_ECF_Daruma(
		pszCargaTributaria.encode('latin-1'),
		pszQuantidade.encode('latin-1'),
		pszPrecoUnitario.encode('latin-1'),
		pszTipoDescAcresc.encode('latin-1'),
		pszValorDescAcresc.encode('latin-1'),
		pszCodigoItem.encode('latin-1'),
		pszUnidadeMedida.encode('latin-1'),
		pszDescricaoItem.encode('latin-1')
	)

def iCFVenderResumido_ECF_Daruma(pszCargaTributaria, pszPrecoUnitario, pszCodigoItem, pszDescricaoItem):
	return __Biblioteca.iCFVenderResumido_ECF_Daruma(
		pszCargaTributaria.encode('latin-1'),
		pszPrecoUnitario.encode('latin-1'),
		pszCodigoItem.encode('latin-1'),
		pszDescricaoItem.encode('latin-1')
	)

def iCFVenderSemDesc_ECF_Daruma(pszCargaTributaria, pszQuantidade, pszPrecoUnitario, pszCodigoItem, pszUnidadeMedida, pszDescricaoItem):
	return __Biblioteca.iCFVenderSemDesc_ECF_Daruma(
		pszCargaTributaria.encode('latin-1'),
		pszQuantidade.encode('latin-1'),
		pszPrecoUnitario.encode('latin-1'),
		pszCodigoItem.encode('latin-1'),
		pszUnidadeMedida.encode('latin-1'),
		pszDescricaoItem.encode('latin-1')
	)

def iCFLancarDescontoItem_ECF_Daruma(pszNumItem, pszTipoDesc, pszValorDesc):
	return __Biblioteca.iCFLancarDescontoItem_ECF_Daruma(
		pszNumItem.encode('latin-1'),
		pszTipoDesc.encode('latin-1'),
		pszValorDesc.encode('latin-1')
	)

def iCFLancarAcrescimoItem_ECF_Daruma(pszNumItem, pszTipoAcresc, pszValorAcresc):
	return __Biblioteca.iCFLancarAcrescimoItem_ECF_Daruma(
		pszNumItem.encode('latin-1'),
		pszTipoAcresc.encode('latin-1'),
		pszValorAcresc.encode('latin-1')
	)

def iCFLancarDescontoUltimoItem_ECF_Daruma(pszTipoDesc, pszValorDesc):
	return __Biblioteca.iCFLancarDescontoUltimoItem_ECF_Daruma(pszTipoDesc.encode('latin-1'), pszValorDesc.encode('latin-1'))

def iCFLancarAcrescimoUltimoItem_ECF_Daruma(pszTipoAcresc, pszValorAcresc):
	return __Biblioteca.iCFLancarAcrescimoUltimoItem_ECF_Daruma(pszTipoAcresc.encode('latin-1'), pszValorAcresc.encode('latin-1'))

def iCFCancelarItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCFCancelarItem_ECF_Daruma(pszNumItem.encode('latin-1'))

def iCFCancelarDescontoItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCFCancelarDescontoItem_ECF_Daruma(pszNumItem.encode('latin-1'))

def iCFCancelarDescontoUltimoItem_ECF_Daruma():
	return __Biblioteca.iCFCancelarDescontoUltimoItem_ECF_Daruma()

def iCFCancelarAcrescimoItem_ECF_Daruma(pszNumItem):
	return __Biblioteca.iCFCancelarAcrescimoItem_ECF_Daruma(pszNumItem.encode('latin-1'))

def iCFCancelarAcrescimoUltimoItem_ECF_Daruma():
	return __Biblioteca.iCFCancelarAcrescimoUltimoItem_ECF_Daruma()

def iCFCancelarDescontoSubtotal_ECF_Daruma():
	return __Biblioteca.iCFCancelarDescontoSubtotal_ECF_Daruma()

def iCFCancelarAcrescimoSubtotal_ECF_Daruma():
	return __Biblioteca.iCFCancelarAcrescimoSubtotal_ECF_Daruma()

def iCFCancelarItemParcial_ECF_Daruma(pszNumItem, pszQuantidade):
	return __Biblioteca.iCFCancelarItemParcial_ECF_Daruma(pszNumItem.encode('latin-1'), pszQuantidade.encode('latin-1'))

def iCFCancelarUltimoItem_ECF_Daruma():
	return __Biblioteca.iCFCancelarUltimoItem_ECF_Daruma()

def iCFCancelarUltimoItemParcial_ECF_Daruma(pszQuantidade):
	return __Biblioteca.iCFCancelarUltimoItemParcial_ECF_Daruma(pszQuantidade.encode('latin-1'))

def iCFTotalizarCupom_ECF_Daruma(pszTipoDescAcresc, pszValorDescAcresc):
	return __Biblioteca.iCFTotalizarCupom_ECF_Daruma(pszTipoDescAcresc.encode('latin-1'), pszValorDescAcresc.encode('latin-1'))

def iCFTotalizarCupomPadrao_ECF_Daruma():
	return __Biblioteca.iCFTotalizarCupomPadrao_ECF_Daruma()

def iCFEfetuarPagamento_ECF_Daruma(psszFormaPgto, pszValor, pszInfoAdicional):
	return __Biblioteca.iCFEfetuarPagamento_ECF_Daruma(
		psszFormaPgto.encode('latin-1'),
		pszValor.encode('latin-1'),
		pszInfoAdicional.encode('latin-1')
	)

def iCFEfetuarPagamentoFormatado_ECF_Daruma(pszFormaPgto, pszValor):
	return __Biblioteca.iCFEfetuarPagamentoFormatado_ECF_Daruma(pszFormaPgto.encode('latin-1'), pszValor.encode('latin-1'))

def iCFEfetuarPagamentoPadrao_ECF_Daruma():
	return __Biblioteca.iCFEfetuarPagamentoPadrao_ECF_Daruma()

def iEstornarPagamento_ECF_Daruma(pszFormaPgtoEstornado, pszFormaPgtoEfetivado, pszValor, pszInfoAdicional):
	return __Biblioteca.iEstornarPagamento_ECF_Daruma(
		pszFormaPgtoEstornado.encode('latin-1'),
		pszFormaPgtoEfetivado.encode('latin-1'),
		pszValor.encode('latin-1'),
		pszInfoAdicional.encode('latin-1')
	)

def iCFIdentificarConsumidor_ECF_Daruma(pszNome, pszEndereco, pszCPF):
	return __Biblioteca.iCFIdentificarConsumidor_ECF_Daruma(
		pszNome.encode('latin-1'),
		pszEndereco.encode('latin-1'),
		pszCPF.encode('latin-1')
	)

def iCFEncerrar_ECF_Daruma(pszCupomAdicional, pszMensagem):
	return __Biblioteca.iCFEncerrar_ECF_Daruma(pszCupomAdicional.encode('latin-1'), pszMensagem.encode('latin-1'))

def iCFEncerrarConfigMsg_ECF_Daruma(pszMensagem):
	return __Biblioteca.iCFEncerrarConfigMsg_ECF_Daruma(pszMensagem.encode('latin-1'))

def iCFEncerrarPadrao_ECF_Daruma():
	return __Biblioteca.iCFEncerrarPadrao_ECF_Daruma()

def iCFEncerrarResumido_ECF_Daruma():
	return __Biblioteca.iCFEncerrarResumido_ECF_Daruma()

def iCFCancelar_ECF_Daruma():
	return __Biblioteca.iCFCancelar_ECF_Daruma()

def iCFEmitirCupomAdicional_ECF_Daruma():
	return __Biblioteca.iCFEmitirCupomAdicional_ECF_Daruma()

def rCFVerificarStatus_ECF_Daruma(pszStatus, piStatus):
	return __Biblioteca.rCFVerificarStatus_ECF_Daruma(byref(c_char_p(pszStatus)), byref(c_int(piStatus)))

def rCMEfetuarCalculo_ECF_Daruma(pszISS, pszICMS):
	return __Biblioteca.rCMEfetuarCalculo_ECF_Daruma(byref(c_char_p(pszISS)), byref(c_char_p(pszICMS)))

''' Gaveta Autentica Outros '''
def eAbrirGaveta_ECF_Daruma():
	return __Biblioteca.eAbrirGaveta_ECF_Daruma()

def eAcionarGuilhotina_ECF_Daruma(pszTipoCorte):
	return __Biblioteca.eAcionarGuilhotina_ECF_Daruma(pszTipoCorte.encode('latin-1'))

def eCarregarBitmapPromocional_ECF_Daruma(pszPathLogotipo, pszNumBitmap, pszOrientacao):
	return __Biblioteca.eCarregarBitmapPromocional_ECF_Daruma(
		pszPathLogotipo.encode('latin-1'),
		pszNumBitmap.encode('latin-1'),
		pszOrientacao.encode('latin-1')
	)

def eSinalSonoro_ECF_Daruma(StrNumeroBeep):
	return __Biblioteca.eSinalSonoro_ECF_Daruma(StrNumeroBeep.encode('latin-1'))

def rStatusGaveta_ECF_Daruma(Int_Status):
	return __Biblioteca.rStatusGaveta_ECF_Daruma(byref(c_int(Int_Status)))

''' Geração de Arquivos '''

def rGerarMFD_ECF_Daruma(szTipo, szInicial, szFinal):
	return __Biblioteca.rGerarMFD_ECF_Daruma(
		pszTipo.encode('latin-1'),
		pszInicial.encode('latin-1'),
		pszFinal.encode('latin-1')
	)

def rGerarNFP_ECF_Daruma(szTipo, szInicial, szFinal):
	return __Biblioteca.rGerarNFP_ECF_Daruma(
		pszTipo.encode('latin-1'),
		pszInicial.encode('latin-1'),
		pszFinal.encode('latin-1')		
	)

def rGerarTDM_ECF_Daruma(szTipo, szInicial, szFinal):
	return __Biblioteca.rGerarTDM_ECF_Daruma(
		pszTipo.encode('latin-1'),
		pszInicial.encode('latin-1'),
		pszFinal.encode('latin-1')		
	)
def rGerarSINTEGRA_ECF_Daruma(szTipo, szInicial, szFinal):
	return __Biblioteca.rGerarSINTEGRA_ECF_Daruma(
		pszTipo.encode('latin-1'),
		pszInicial.encode('latin-1'),
		pszFinal.encode('latin-1')
	)

def rGerarSPED_ECF_Daruma(szTipo, szInicial, szFinal):
	return __Biblioteca.rGerarSPED_ECF_Daruma(
		pszTipo.encode('latin-1'),
		pszInicial.encode('latin-1'),
		pszFinal.encode('latin-1')		
	)

def rGerarEspelhoMFD_ECF_Daruma(pszTipo, pszInicial, pszFinal):
	return __Biblioteca.rGerarEspelhoMFD_ECF_Daruma(
		pszTipo.encode('latin-1'),
		pszInicial.encode('latin-1'),
		pszFinal.encode('latin-1')
	)

def rGerarRelatorio_ECF_Daruma(szRelatorio, szTipo, pszInicial, pszFinal):
	return __Biblioteca.rGerarRelatorio_ECF_Daruma(
		byref(c_char_p(szRelatorio)),
		byref(c_char_p(szTipo)),
		byref(c_char_p(pszInicial)),
		byref(c_char_p(pszFinal))
	)

def rGerarRelatorioOffline_ECF_Daruma(szRelatorio, szTipo, pszInicial, pszFinal, szArquivo_MF, szArquivo_MFD, szArquivo_INF):
	return __Biblioteca.rGerarRelatorioOffline_ECF_Daruma(
		szRelatorio.encode('latin-1'),
		szTipo.encode('latin-1'),
		pszInicial.encode('latin-1'),
		pszInicial.encode('latin-1'),
		szArquivo_MF.encode('latin-1'),
		szArquivo_MFD.encode('latin-1'),
		szArquivo_INF.encode('latin-1')
	)

def rGerarMapaResumo_ECF_Daruma():
	return __Biblioteca.rGerarMapaResumo_ECF_Daruma()

def rEfetuarDownloadMFD_ECF_Daruma(pszTipo, pszInicial, pszFinal, pszNomeArquivo):
	return __Biblioteca.rEfetuarDownloadMFD_ECF_Daruma(
		pszTipo.encode('latin-1'),
		pszInicial.encode('latin-1'),
		pszFinal.encode('latin-1'),
		pszNomeArquivo.encode('latin-1')
	)

def rEfetuarDownloadMF_ECF_Daruma(pszNomeArquivo):
	return __Biblioteca.rEfetuarDownloadMF_ECF_Daruma(pszNomeArquivo.encode('latin-1'))

''' Lei DE OLHO no Imposto '''
def confCFNCM_ECF_Daruma(pszNCM, pszTipoOrigem):
	return __Biblioteca.confCFNCM_ECF_Daruma(pszNCM.encode('latin-1'), pszTipoOrigem.encode('latin-1'))

def rCFVrImposto_ECF_Daruma(pszNumeroItem, pszVrImposto):
	return __Biblioteca.rCFVrImposto_ECF_Daruma(pszNumeroItem.encode('latin-1'), pszVrImposto.encode('latin-1'))

 #''' PAF-ECF '''
def ePAFCadastrar_ECF_Daruma(pszNomeArquivo, pszChave, pszNumSerieECF, pszGT):
	return __Biblioteca.ePAFCadastrar_ECF_Daruma(
		pszNomeArquivo.encode('latin-1'),
		pszChave.encode('latin-1'),
		pszNumSerieECF.encode('latin-1'),
		pszGT.encode('latin-1')
	)

def ePAFValidarDados_ECF_Daruma(pszNomeArquivo, pszChave, pszNumSerieEFC, pszGT):
	return __Biblioteca.ePAFValidarDados_ECF_Daruma(
		pszNomeArquivo.encode('latin-1'),
		pszChave.encode('latin-1'),
		pszNumSerieEFC.encode('latin-1'),
		pszGT.encode('latin-1')
	)

def ePAFAtualizarGT_ECF_Daruma(pszNomeArquivo, pszChave, pszNumSerieECF, pszGT):
	return __Biblioteca.ePAFAtualizarGT_ECF_Daruma(
		pszNomeArquivo.encode('latin-1'),
		pszChave.encode('latin-1'),
		pszNumSerieECF.encode('latin-1'),
		pszGT.encode('latin-1')
	)

def confModoPAF_ECF_Daruma(pszAtivar, pszChave, pszNomeArquivo):
	return __Biblioteca.confModoPAF_ECF_Daruma(
		pszAtivar.encode('latin-1'),
		pszChave.encode('latin-1'),
		pszNomeArquivo.encode('latin-1')
	)

def rLerArqRegistroPAF_ECF_Daruma(pszCaminho, pszChave, pszReturn):
	return __Biblioteca.rLerArqRegistroPAF_ECF_Daruma(
		pszCaminho.encode('latin-1'),
		pszChave.encode('latin-1'),
		pszReturn.encode('latin-1')
	)

def eRSAAssinarArquivo_ECF_Daruma(szArquivo, szChavePrivada):
	return __Biblioteca.eRSAAssinarArquivo_ECF_Daruma(
		byref(c_char_p(szArquivo)),
		szChavePrivada.encode('latin-1'))

def rAssinarRSA_ECF_Daruma(pszPathArquivo, pszChavePrivada, pszAssinaturaGerada):
	return __Biblioteca.rAssinarRSA_ECF_Daruma(
		pszPathArquivo.encode('latin-1'),
		pszChavePrivada.encode('latin-1'),
		byref(c_char_p(pszAssinaturaGerada))
	)

def rRSAChavePublica_ECF_Daruma(szChavePrivada, szChavePublica, szExpoenteszExpoente):
	return __Biblioteca.rRSAChavePublica_ECF_Daruma(
		szChavePrivada.encode('latin-1'),
		byref(c_char_p(szChavePublica)),
		byref(c_char_p(szExpoenteszExpoente))
	)

def rCalcularMD5_ECF_Daruma(pszPathArquivo, pszMD5GeradoHex, pszMD5GeradoAscii):
	return __Biblioteca.rCalcularMD5_ECF_Daruma(
		pszPathArquivo.encode('latin-1'),
		pszMD5GeradoHex.encode('latin-1'),
		pszMD5GeradoAscii.encode('latin-1')
	)

def rCodigoModeloFiscal_ECF_Daruma(pszValor):
	return __Biblioteca.rCodigoModeloFiscal_ECF_Daruma(pszValor.encode('latin-1'))

def rRetornarGTCodificado_ECF_Daruma(pszValor):
	return __Biblioteca.rRetornarGTCodificado_ECF_Daruma(pszValor.encode('latin-1'))

def rRetornarNumeroSerieCodificado_ECF_Daruma(pszValor):
	return __Biblioteca.rRetornarNumeroSerieCodificado_ECF_Daruma(pszValor.encode('latin-1'))

def rVerificarGTCodificado_ECF_Daruma(pszValor):
	return __Biblioteca.rVerificarGTCodificado_ECF_Daruma(pszValor.encode('latin-1'))

def rVerificarNumeroSerieCodificado_ECF_Daruma(pszValor):
	return __Biblioteca.rVerificarNumeroSerieCodificado_ECF_Daruma(pszValor.encode('latin-1'))

def eMemoriaFiscal_ECF_Daruma(pszInicial, pszFinal, pszCompleta, pszTipo):
	return __Biblioteca.eMemoriaFiscal_ECF_Daruma(
		pszInicial.encode('latin-1'),
		pszFinal.encode('latin-1'),
		pszCompleta.encode('latin-1'),
		pszTipo.encode('latin-1')
	)

''' Registry '''
def regCFCupomAdicionalDllConfig_ECF_Daruma(pszParametro):
	return __Biblioteca.regCFCupomAdicionalDllConfig_ECF_Daruma(pszParametro.encode('latin-1'))

def regSintegra_ECF_Daruma(pszPathChave, pszValor):
	return __Biblioteca.regSintegra_ECF_Daruma(pszPathChave.encode('latin-1'), pszValor.encode('latin-1'))

''' Relatorio Gerencial '''
def iRGAbrir_ECF_Daruma(pszNomeRG):
	return __Biblioteca.iRGAbrir_ECF_Daruma(pszNomeRG.encode('latin-1'))

def iRGAbrirIndice_ECF_Daruma(pszIndiceRG):
	return __Biblioteca.iRGAbrirIndice_ECF_Daruma(pszIndiceRG)

def iRGAbrirPadrao_ECF_Daruma():
	return __Biblioteca.iRGAbrirPadrao_ECF_Daruma()

def iRGImprimirTexto_ECF_Daruma(pszArquivo):
	return __Biblioteca.iRGImprimirTexto_ECF_Daruma(pszArquivo.encode('latin-1'))

def iRGImprimirArquivo_ECF_Daruma(pszArquivo):
	return __Biblioteca.iRGImprimirArquivo_ECF_Daruma(pszArquivo.encode('latin-1'))

def iRGFechar_ECF_Daruma():
	return __Biblioteca.iRGFechar_ECF_Daruma()

def rRGVerificarStatus_ECF_Daruma(pszStatus):
	return __Biblioteca.rRGVerificarStatus_ECF_Daruma(byref(c_char_p(pszStatus)))

''' Relatorios Fiscais '''
def iLeituraX_ECF_Daruma():
	return __Biblioteca.iLeituraX_ECF_Daruma()

def rLeituraX_ECF_Daruma():
	return __Biblioteca.rLeituraX_ECF_Daruma()

def rLeituraXCustomizada_ECF_Daruma(pszCaminho):
	return __Biblioteca.rLeituraXCustomizada_ECF_Daruma(pszCaminho.encode('latin-1'))

def iMFLer_ECF_Daruma(pszInicial, pszFinal):
	return __Biblioteca.iMFLer_ECF_Daruma(pszInicial.encode('latin-1'), pszFinal.encode('latin-1'))

def iMFLerSerial_ECF_Daruma(pszInicial, pszFinal):
	return __Biblioteca.iMFLerSerial_ECF_Daruma(pszInicial.encode('latin-1'), pszFinal.encode('latin-1'))

def iSangria_ECF_Daruma(pszValor, pszMensagem):
	return __Biblioteca.iSangria_ECF_Daruma(pszValor.encode('latin-1'), pszMensagem.encode('latin-1'))

def iSangriaPadrao_ECF_Daruma():
	return __Biblioteca.iSangriaPadrao_ECF_Daruma()

def iSuprimento_ECF_Daruma(pszValor, pszMensagem):
	return __Biblioteca.iSuprimento_ECF_Daruma(pszValor.encode('latin-1'), pszMensagem.encode('latin-1'))

def iSuprimentoPadrao_ECF_Daruma():
	return __Biblioteca.iSuprimentoPadrao_ECF_Daruma()

def iRelatorioConfiguracao_ECF_Daruma():
	return __Biblioteca.iRelatorioConfiguracao_ECF_Daruma()

def iReducaoZ_ECF_Daruma(pszData, pszHora):
	return __Biblioteca.iReducaoZ_ECF_Daruma(pszData.encode('latin-1'), pszHora.encode('latin-1'))

''' Retornos e Status '''
def eBuscarPortaVelocidade_ECF_Daruma():
	return __Biblioteca.eBuscarPortaVelocidade_ECF_Daruma()

def eRetornarPortasCOM_ECF_Daruma(pszRetorno):
	return __Biblioteca.eRetornarPortasCOM_ECF_Daruma(byref(c_char_p(pszRetorno)))

def eInterpretarRetorno_ECF_Daruma(iIndice, pszRetorno):
	return __Biblioteca.eInterpretarRetorno_ECF_Daruma(iIndice, byref(c_char_p(pszRetorno)))

def eInterpretarAviso_ECF_Daruma(iIndice, pszRetorno):
	return __Biblioteca.eInterpretarAviso_ECF_Daruma(iIndice, byref(c_char_p(pszRetorno)))

def eInterpretarErro_ECF_Daruma(iIndice, pszRetorno):
	return __Biblioteca.eInterpretarErro_ECF_Daruma(iIndice, byref(c_char_p(pszRetorno)))

def eRetornarAvisoErroUltimoCMD_ECF_Daruma(Str_Aviso, Str_Erro):
	return __Biblioteca.eRetornarAvisoErroUltimoCMD_ECF_Daruma(byref(c_char_p(Str_Aviso)), byref(c_char_p(Str_Erro)))

def rStatusImpressora_ECF_Daruma(pszStatus):
	return __Biblioteca.rStatusImpressora_ECF_Daruma(byref(c_char_p(pszStatus)))

def rStatusImpressoraBinario_ECF_Daruma(pszStatus):
	return __Biblioteca.rStatusImpressoraBinario_ECF_Daruma(byref(c_char_p(pszStatus)))

def rConsultaStatusImpressoraInt_ECF_Daruma(iIndice, iRetorno):
	return __Biblioteca.rConsultaStatusImpressoraInt_ECF_Daruma(iIndice, byref(c_int(iRetorno)))

def rConsultaStatusImpressoraStr_ECF_Daruma(iIndice, szStatus):
	return __Biblioteca.rConsultaStatusImpressoraStr_ECF_Daruma(iIndice, byref(c_char_p(szStatus)))

def rStatusUltimoCmd_ECF_Daruma(pszErro, pszAviso, piErro, piAviso):
	return __Biblioteca.rStatusUltimoCmd_ECF_Daruma(
		byref(c_char_p(pszErro)),
		byref(c_char_p(pszAviso)),
		byref(c_int(piErro)),
		byref(c_int(piAviso))
	)

def rStatusUltimoCmdInt_ECF_Daruma(iErro, iAviso):
	return __Biblioteca.rStatusUltimoCmdInt_ECF_Daruma(byref(c_int(iErro)), byref(c_int(iAviso)))

def rStatusUltimoCmdStr_ECF_Daruma(pszErro, pszAviso):
	return __Biblioteca.rStatusUltimoCmdStr_ECF_Daruma(byref(c_char_p(pszErro)), byref(c_char_p(pszAviso)))

def rInfoEstendida_ECF_Daruma(indice, pszRetorno):
	return __Biblioteca.rInfoEstendida_ECF_Daruma(indice, byref(c_char_p(pszRetorno)))

def rInfoEstendida1_ECF_Daruma(pszInfo1):
	return __Biblioteca.rInfoEstendida1_ECF_Daruma(byref(c_char_p(pszInfo1)))

def rInfoEstendida2_ECF_Daruma(pszInfo2):
	return __Biblioteca.rInfoEstendida2_ECF_Daruma(byref(c_char_p(pszInfo2)))

def rInfoEstendida3_ECF_Daruma(pszInfo3):
	return __Biblioteca.rInfoEstendida3_ECF_Daruma(byref(c_char_p(pszInfo3)))

def rInfoEstendida4_ECF_Daruma(pszInfo4):
	return __Biblioteca.rInfoEstendida4_ECF_Daruma(byref(c_char_p(pszInfo4)))

def rInfoEstendida5_ECF_Daruma(pszInfo5):
	return __Biblioteca.rInfoEstendida5_ECF_Daruma(byref(c_char_p(pszInfo5)))

def rRetornarInformacao_ECF_Daruma(pszIndice, pszRetornar):
	return __Biblioteca.rRetornarInformacao_ECF_Daruma(pszIndice.encode('latin-1'), byref(c_char_p(pszRetornar)))

def rRetornarInformacaoSeparador_ECF_Daruma(pszIndice, pszVSignificativo, pszRetornar):
	return __Biblioteca.rRetornarInformacaoSeparador_ECF_Daruma(
		pszIndice.encode('latin-1'), 
		pszVSignificativo.encode('latin-1'), 
		byref(c_char_p(pszRetornar))
	)

def rLerAliquotas_ECF_Daruma(cAliquotas):
	return __Biblioteca.rLerAliquotas_ECF_Daruma(byref(c_char_p(cAliquotas)))

def rLerMeiosPagto_ECF_Daruma(pszRelatorios):
	return __Biblioteca.rLerMeiosPagto_ECF_Daruma(byref(c_char_p(pszRelatorios)))

def rLerRG_ECF_Daruma(pszRelatorios):
	return __Biblioteca.rLerRG_ECF_Daruma(byref(c_char_p(pszRelatorios)))

def rLerCNF_ECF_Daruma(pszTotalizadores):
	return __Biblioteca.rLerCNF_ECF_Daruma(byref(c_char_p(pszTotalizadores)))

def rInfoCNF_ECF_Daruma(pszRetorno):
	return __Biblioteca.rInfoCNF_ECF_Daruma(byref(c_char_p(pszRetorno)))

def rLerDecimais_ECF_Daruma(pszDecimalQtde, pszDecimalValor, piDecimalQtde, piDecimalValor):
	return __Biblioteca.rLerDecimais_ECF_Daruma(
		byref(c_char_p(pszDecimalQtde)),
		byref(c_char_p(pszDecimalValor)),
		byref(c_int(piDecimalQtde)),
		byref(c_int(piDecimalValor))
	)

def rLerDecimaisInt_ECF_Daruma(piDecimalQtde, piDecimalValor):
	return __Biblioteca.rLerDecimaisInt_ECF_Daruma(byref(c_int(piDecimalQtde)), byref(c_int(piDecimalValor)))

def rLerDecimaisStr_ECF_Daruma(pszDecimalQtde, pszDecimalValor):
	return __Biblioteca.rLerDecimaisStr_ECF_Daruma(byref(c_char_p(pszDecimalQtde)), byref(c_char_p(pszDecimalValor)))

def rCompararDataHora_ECF_Daruma(iDiferenca):
	return __Biblioteca.rCompararDataHora_ECF_Daruma(byref(c_int(iDiferenca)))

def rDataHoraImpressora_ECF_Daruma(pszData, pszHora):
	return __Biblioteca.rDataHoraImpressora_ECF_Daruma(byref(c_char_p(pszData)), byref(c_char_p(pszHora)))

def rVerificarImpressoraLigada_ECF_Daruma():
	return __Biblioteca.rVerificarImpressoraLigada_ECF_Daruma()

def rVerificarReducaoZ_ECF_Daruma(pszPendente):
	return __Biblioteca.rVerificarReducaoZ_ECF_Daruma(byref(c_char_p(pszPendente)))

def rRetornarDadosReducaoZ_ECF_Daruma(pszRetorno):
	return __Biblioteca.rRetornarDadosReducaoZ_ECF_Daruma(byref(c_char_p(pszRetorno)))

def rTipoUltimoDocumentoInt_ECF_Daruma(iDoc):
	return __Biblioteca.rTipoUltimoDocumentoInt_ECF_Daruma(byref(c_int(iDoc)))

def rTipoUltimoDocumentoStr_ECF_Daruma(pszDoc):
	return __Biblioteca.rTipoUltimoDocumentoStr_ECF_Daruma(byref(c_char_p(pszDoc)))

def rUltimoCMDEnviado_ECF_Daruma(pszComando):
	return __Biblioteca.rUltimoCMDEnviado_ECF_Daruma(byref(c_char_p(pszComando)))

def rMinasLegal_ECF_Daruma(pszRetorno):
	return __Biblioteca.rMinasLegal_ECF_Daruma(byref(c_char_p(pszRetorno)))

def rRetornarVendaBruta_ECF_Daruma(pszRetorno):
	return __Biblioteca.rRetornarVendaBruta_ECF_Daruma(byref(c_char_p(pszRetorno)))

def rRetornarVendaLiquida_ECF_Daruma(pszVendaLiquida):
	return __Biblioteca.rRetornarVendaLiquida_ECF_Daruma(byref(c_char_p(pszVendaLiquida)))

def rCFSaldoAPagar_ECF_Daruma(pszValor):
	return __Biblioteca.rCFSaldoAPagar_ECF_Daruma(byref(c_char_p(pszValor)))

def rCFSubTotal_ECF_Daruma(pszValor):
	return __Biblioteca.rCFSubTotal_ECF_Daruma(byref(c_char_p(pszValor)))	

''' WebService '''
def eWsEnviarCupom_ECF_Daruma(pszCPF, pszNomeFantasia, pszIndiceSegmento, pszCCF, pszData, pszHora, pszValor, pszISS, pszICMS, szReservado, iRespostaWS):
	return __Biblioteca.eWsEnviarCupom_ECF_Daruma(
		pszCPF.encode('latin-1'),
		pszNomeFantasia.encode('latin-1'),
		pszIndiceSegmento.encode('latin-1'),
		pszCCF.encode('latin-1'),
		pszData.encode('latin-1'),
		pszHora.encode('latin-1'),
		pszValor.encode('latin-1'),
		pszISS.encode('latin-1'),
		pszICMS.encode('latin-1'),
		c_short(szReservado),
		byref(c_int(iRespostaWS))
	)

def eWsStatus_ECF_Daruma(iRespostaWS):
	return __Biblioteca.eWsStatus_ECF_Daruma(byref(c_int(iRespostaWS)))

''' Métodos do modulo DUAL '''
def regAguardarProcesso_DUAL_DarumaFramework(valor):
	return __Biblioteca.regAguardarProcesso_DUAL_DarumaFramework(valor.encode('latin-1'))

def regCodePageAutomatico_DUAL_DarumaFramework(valor):
	return __Biblioteca.regCodePageAutomatico_DUAL_DarumaFramework(valor.encode('latin-1'))

def regEnterFinal_DUAL_DarumaFramework(valor):
	return __Biblioteca.regEnterFinal_DUAL_DarumaFramework(valor.encode('latin-1'))

def regInicializou_DUAL_DarumaFramework(valor):
	return __Biblioteca.regInicializou_DUAL_DarumaFramework(valor.encode('latin-1'))

def regLinhasGuilhotina_DUAL_DarumaFramework(valor):
	return __Biblioteca.regLinhasGuilhotina_DUAL_DarumaFramework(valor.encode('latin-1'))

def regModoGaveta_DUAL_DarumaFramework(gavetastatus):
	return __Biblioteca.regModoGaveta_DUAL_DarumaFramework(gavetastatus.encode('latin-1'))

def regPortaComunicacao_DUAL_DarumaFramework(valor):
	return __Biblioteca.regPortaComunicacao_DUAL_DarumaFramework(valor.encode('latin-1'))

def regTabulacao_DUAL_DarumaFramework(valor):
	return __Biblioteca.regTabulacao_DUAL_DarumaFramework(valor.encode('latin-1'))

def regTermica_DUAL_DarumaFramework(valor):
	return __Biblioteca.regTermica_DUAL_DarumaFramework(valor.encode('latin-1'))

def regVelocidade_DUAL_DarumaFramework(valor):
	return __Biblioteca.regVelocidade_DUAL_DarumaFramework(valor.encode('latin-1'))

def regZeroCortado_DUAL_DarumaFramework(valor):
	return __Biblioteca.regZeroCortado_DUAL_DarumaFramework(valor.encode('latin-1'))

def rConsultaStatusImpressora_DUAL_DarumaFramework(indice, tipo, impressoraStatus):
	return __Biblioteca.rConsultaStatusImpressora_DUAL_DarumaFramework(
		indice.encode('latin-1'), 
		tipo.encode('latin-1'), 
		c_char_p(impressoraStatus)
	)

def rStatusDocumento_DUAL_DarumaFramework():
	return __Biblioteca.rStatusDocumento_DUAL_DarumaFramework()

def rStatusGaveta_DUAL_DarumaFramework(gavetaStatus):
	return __Biblioteca.rStatusGaveta_DUAL_DarumaFramework(byref(c_int(gavetaStatus)))

def rStatusImpressora_DUAL_DarumaFramework():
	return __Biblioteca.rStatusImpressora_DUAL_DarumaFramework()

def rStatusGuilhotina_DUAL_DarumaFramework():
	return __Biblioteca.rStatusGuilhotina_DUAL_DarumaFramework()

def iAcionarGaveta_DUAL_DarumaFramework():
	return __Biblioteca.iAcionarGaveta_DUAL_DarumaFramework()

def iAutenticarDocumento_DUAL_DarumaFramework(documento, local, timeout):
	return __Biblioteca.iAutenticarDocumento_DUAL_DarumaFramework(
		documento, 
		local, 
		timeout
	)

def iImprimirArquivo_DUAL_DarumaFramework(arquivo):
	return __Biblioteca.iImprimirArquivo_DUAL_DarumaFramework(arquivo.encode('latin-1'))

def iImprimirTexto_DUAL_DarumaFramework(texto, tamanhoTexto):
	return __Biblioteca.iImprimirTexto_DUAL_DarumaFramework(
		texto.encode('latin-1'), 
		c_int(tamanhoTexto)
	)

def iConfigurarGuilhotina_DUAL_DarumaFramework(habilitar, quantidadeLinha):
	return __Biblioteca.iConfigurarGuilhotina_DUAL_DarumaFramework(
		habilitar.encode('latin-1'), 
		quantidadeLinha.encode('latin-1')
	)

def iEnviarBMP_DUAL_DarumaFramework(arquivoOrigem):
	return __Biblioteca.iEnviarBMP_DUAL_DarumaFramework(arquivoOrigem.encode('latin-1'))

def iLimparBuffer_DUAL_DarumaFramework():
	return __Biblioteca.iLimparBuffer_DUAL_DarumaFramework()

def iReinicializar_DUAL_DarumaFramework():
	return __Biblioteca.iReinicializar_DUAL_DarumaFramework()

''' Métodos do modulo MODEM '''
def eAtivarConexaoCsd_MODEM_DarumaFramework():
	return __Biblioteca.eAtivarConexaoCsd_MODEM_DarumaFramework()

def eApagarSms_MODEM_DarumaFramework(indice):
	return __Biblioteca.eApagarSms_MODEM_DarumaFramework(indice.encode('latin-1'))

def eFinalizarChamadaCsd_MODEM_DarumaFramework():
	return __Biblioteca.eFinalizarChamadaCsd_MODEM_DarumaFramework()

def eReiniciar_MODEM_DarumaFramework():
	return __Biblioteca.eReiniciar_MODEM_DarumaFramework()

def eInicializar_MODEM_DarumaFramework():
	return __Biblioteca.eInicializar_MODEM_DarumaFramework()

def eRealizarChamadaCsd_MODEM_DarumaFramework(telefone):
	return __Biblioteca.eRealizarChamadaCsd_MODEM_DarumaFramework(telefone.encode('latin-1'))

def eTrocarBandeja_MODEM_DarumaFramework():
	return __Biblioteca.eTrocarBandeja_MODEM_DarumaFramework()

def regLerApagar_MODEM_DarumaFramework(valor):
	return __Biblioteca.regLerApagar_MODEM_DarumaFramework(valor.encode('latin-1'))

def regPorta_MODEM_DarumaFramework(valor):
	return __Biblioteca.regPorta_MODEM_DarumaFramework(valor.encode('latin-1'))

def regThread_MODEM_DarumaFramework(valor):
	return __Biblioteca.regThread_MODEM_DarumaFramework(valor.encode('latin-1'))

def regVelocidade_MODEM_DarumaFramework(valor):
	return __Biblioteca.regVelocidade_MODEM_DarumaFramework(valor.encode('latin-1'))

def regCaptionWinAPP_MODEM_DarumaFramework(valor):
	return __Biblioteca.regCaptionWinAPP_MODEM_DarumaFramework(valor.encode('latin-1'))

def regBandejaInicio_MODEM_DarumaFramework(valor):
	return __Biblioteca.regBandejaInicio_MODEM_DarumaFramework(valor.encode('latin-1'))

def regTempoAlertar_MODEM_DarumaFramework(valor):
	return __Biblioteca.regTempoAlertar_MODEM_DarumaFramework(valor.encode('latin-1'))

def rReceberSms_MODEM_DarumaFramework(indice, mensagem, data, hora, remetente):
	return __Biblioteca.rReceberSms_MODEM_DarumaFramework(
		indice.encode('latin-1'), 
		mensagem.encode('latin-1'), 
		data.encode('latin-1'), 
		hora.encode('latin-1'), 
		remetente.encode('latin-1')
	)

def rReceberSmsIndice_MODEM_DarumaFramework(indice, mensagem, data, hora, remetente):
	return __Biblioteca.rReceberSmsIndice_MODEM_DarumaFramework(
		indice.encode('latin-1'), 
		mensagem.encode('latin-1'), 
		data.encode('latin-1'), 
		hora.encode('latin-1'), 
		remetente.encode('latin-1')		
	)

def rRetornarImei_MODEM_DarumaFramework(imei):
	return __Biblioteca.rRetornarImei_MODEM_DarumaFramework(imei.encode('latin-1'))

def rRetornarOperadora_MODEM_DarumaFramework(operadora):
	return __Biblioteca.rRetornarOperadora_MODEM_DarumaFramework(operadora.encode('latin-1'))

def rReceberDadosCsd_MODEM_DarumaFramework(resposta):
	return __Biblioteca.rReceberDadosCsd_MODEM_DarumaFramework(resposta.encode('latin-1'))

def rNivelSinalRecebido_MODEM_DarumaFramework():
	return __Biblioteca.rNivelSinalRecebido_MODEM_DarumaFramework()

def rListarSms_MODEM_DarumaFramework():
	return __Biblioteca.rListarSms_MODEM_DarumaFramework()

def tEnviarDadosCsd_MODEM_DarumaFramework(dados):
	return __Biblioteca.tEnviarDadosCsd_MODEM_DarumaFramework(dados.encode('latin-1'))

def tEnviarSms_MODEM_DarumaFramework(telefone, mensagem):
	return __Biblioteca.tEnviarSms_MODEM_DarumaFramework(
		telefone.encode('latin-1'), 
		mensagem.encode('latin-1')
	)

def tEnviarSmsOperadora_MODEM_DarumaFramework(telefone, bandeja, mensagem):
	return __Biblioteca.tEnviarSmsOperadora_MODEM_DarumaFramework(
		telefone.encode('latin-1'), 
		bandeja.encode('latin-1'), 
		mensagem.encode('latin-1')
	)

def eBuscarPortaVelocidade_MODEM_DarumaFramework():
	return __Biblioteca.eBuscarPortaVelocidade_MODEM_DarumaFramework()