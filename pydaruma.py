

class DarumaECF:
		"""docstring for DarumaECF"""
		def __init__(self, arg):
			super(DarumaECF, self).__init__()
			self.arg = arg

		# Bilhete de passagem
		def confCFBPProgramarUF_ECF_Daruma(self, pszUF):
		 	return confCFBPProgramarUF_ECF_Daruma(pszUF.encode('ascii'))

		def iCFBPAbrir_ECF_Daruma(self, pszOrigem, pszDestino, pszUFDestino, pszPercurso, pszPrestadora, pszPlataforma, pszPoltrona, pszModalidadetransp, pszCategoriaTransp, pszDataEmbarque, pszRGPassageiro, pszNomePassageiro, pszEnderecoPassageiro):
		 	return iCFBPAbrir_ECF_Daruma(
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

		def iCFBPVender_ECF_Daruma(self, pszCargaTributaria, pszPrecoUnitario, pszTipoDescAcresc, pszValorDescAcresc, pszDescricaoItem):
		 	return iCFBPVender_ECF_Daruma(
				pszCargaTributaria.encode('ascii'),
				pszPrecoUnitario.encode('ascii'),
				pszTipoDescAcresc.encode('ascii'),
				pszValorDescAcresc.encode('ascii'),
				pszDescricaoItem.encode('ascii')
		 	)

		# Cheque
		def confCorrigirGeometria_CHEQUE_Daruma(self, pszNumeroBanco, pszDistValorNumerico, pszColunaValorNumerico, pszDistPrimExtenso, pszColunaPrimExtenso, pszDistSegExtenso, pszColunaSegExtenso, pszDistFavorecido, pszColunaFavorecido, pszDistCidade, pszColunaCidade, pszColunaDia, pszColunaMes, pszColunaAno, pszLinhaAutenticacao, pszColunaAutenticacao):
		 	return confCorrigirGeometria_CHEQUE_Daruma(
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

		def iAtributo_CHEQUE_Daruma(self, pszModo):
		 	return iAtributo_CHEQUE_Daruma(pszModo.encode('ascii'))

		def iAutenticar_CHEQUE_Daruma(self, pszPosicao, pszTexto):
		 	return iAutenticar_CHEQUE_Daruma(pszPosicao.encode('ascii'), pszTexto.encode('ascii'))

		def iImprimir_CHEQUE_Daruma(self, pszNumeroBanco, pszCidade, pszData, pszNomeFavorecido, pszTextoFrente, pszValorCheque):
		 	return iImprimir_CHEQUE_Daruma(
		 		pszNumeroBanco.encode('ascii'),
		 		pszCidade.encode('ascii'),
		 		pszData.encode('ascii'),
		 		pszNomeFavorecido.encode('ascii'),
		 		pszTextoFrente.encode('ascii'),
		 		pszValorCheque.encode('ascii')
		 	)

		def iImprimirVerso_CHEQUE_Daruma(self, pszTexto):
		 	return iImprimirVerso_CHEQUE_Daruma(pszTexto.encode('ascii'))

		def iImprimirVertical_CHEQUE_Daruma(self, pszNumeroBanco, pszCidade, pszData, pszNomeFavorecido, pszTextoFrente, pszValorCheque):
		 	return iImprimirVertical_CHEQUE_Daruma(
		 		pszNumeroBanco.encode('ascii'),
		 		 pszCidade.encode('ascii'),
		 		 pszData.encode('ascii'),
		 		 pszNomeFavorecido.encode('ascii'),
		 		 pszTextoFrente.encode('ascii'),
		 		 pszValorCheque.encode('ascii')
		 	)

		def eEjetarCheque_ECF_Daruma(self):
		 	return eEjetarCheque_ECF_Daruma()

		# Código de barras
		def iImprimirCodigoBarras_ECF_Daruma(self, pszTipo, pszLargura, pszAltura, pszImprTexto, pszCodigo, pszOrientacao, pszTextoLivre):
			return iImprimirCodigoBarras_ECF_Daruma(
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
		def eTEF_EsperarArquivo_ECF_Daruma(self, szArquivo, iTempo, bTravarTeclado):
		 	return eTEF_EsperarArquivo_ECF_Daruma(
		 		szArquivo.encode('ascii'),
		 		iTempo,
		 		bTravarTeclado
		 	)

		def eTEF_SetarFoco_ECF_Daruma(self, szNomeTela):
		 	return eTEF_SetarFoco_ECF_Daruma(szNomeTela.encode('ascii'))

		def eTEF_TravarTeclado_ECF_Daruma(self, bTravarTeclado):
		 	return eTEF_TravarTeclado_ECF_Daruma(bTravarTeclado)

		def iTEF_ImprimirResposta_ECF_Daruma(self, szArquivo, bTravarTeclado):
		 	return iTEF_ImprimirResposta_ECF_Daruma(szArquivo.encode('ascii'), bTravarTeclado)

		def iTEF_ImprimirRespostaCartao_ECF_Daruma(self, szArquivo, bTravarTeclado, szForma, szValor):
		 	return iTEF_ImprimirRespostaCartao_ECF_Daruma(
		 		szArquivo.encode('ascii'),
		 		bTravarTeclado,
		 		szForma.encode('ascii'),
		 		szValor.encode('ascii')
		 	)

		def iTEF_Fechar_ECF_Daruma(self):
		 	return iTEF_Fechar_ECF_Daruma()		 	
		# Funções TEF - Fim

		def iCCDAbrir_ECF_Daruma(self, pszFormaPgto, pszParcelas, pszDocOrigem, pszValor, pszCPF, pszNome, pszEndereco):
		 	return iCCDAbrir_ECF_Daruma(
		 		pszFormaPgto.encode('ascii'),
		 		pszParcelas.encode('ascii'),
		 		pszDocOrigem.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszCPF.encode('ascii'),
		 		pszNome.encode('ascii'),
		 		pszEndereco.encode('ascii')
		 	)

		def iCCDAbrirPadrao_ECF_Daruma(self):
		 	return iCCDAbrirPadrao_ECF_Daruma()

		def iCCDAbrirSimplificado_ECF_Daruma(self, pszFormaPgto, pszParcelas, pszDocOrigem, pszValor):
		 	return iCCDAbrirSimplificado_ECF_Daruma(pszFormaPgto,
		 		pszParcelas.encode('ascii'),
		 		pszDocOrigem.encode('ascii'),
		 		pszValor.encode('ascii')
		 	)

		def iCCDImprimirTexto_ECF_Daruma(self, pszTexto):
		 	return iCCDImprimirTexto_ECF_Daruma(pszTexto.encode('ascii'))

		def iCCDImprimirArquivo_ECF_Daruma(self, pszArqOrigem):
		 	return iCCDImprimirArquivo_ECF_Daruma(pszArqOrigem.encode('ascii'))

		def iCCDEstornar_ECF_Daruma(self, pszCOO, pszCPF, pszNome, pszEndereco):
		 	return iCCDEstornar_ECF_Daruma(
		 		pszCOO.encode('ascii'),
		 		 pszCPF.encode('ascii'),
		 		 pszNome.encode('ascii'),
		 		 pszEndereco.encode('ascii')
		 	)

		def iCCDEstornarPadrao_ECF_Daruma(self):
		 	return iCCDEstornarPadrao_ECF_Daruma()

		def iCCDFechar_ECF_Daruma(self):
		 	return iCCDFechar_ECF_Daruma()

		def iCCDSegundaVia_ECF_Daruma(self):
		 	return iCCDSegundaVia_ECF_Daruma()
		
		# Comprovante Não Fiscal
		def iCNFAbrir_ECF_Daruma(self, pszCPF, pszNome, pszEndereco):
		 	return iCNFAbrir_ECF_Daruma(
		 		pszCPF.encode('ascii'),
		 		pszNome.encode('ascii'),
		 		pszEndereco.encode('ascii')
		 	)

		def iCNFAbrirPadrao_ECF_Daruma(self):
		 	return iCNFAbrirPadrao_ECF_Daruma()

		def iCNFReceber_ECF_Daruma(self, pszIndice, pszValor, pszTipoDescAcresc, pszValorDescAcresc):
		 	return iCNFReceber_ECF_Daruma(
		 		pszIndice.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszTipoDescAcresc.encode('ascii'),
		 		pszValorDescAcresc.encode('ascii')
		 	)

		def iCNFReceberSemDesc_ECF_Daruma(self, pszIndice, pszValor):
		 	return iCNFReceberSemDesc_ECF_Daruma(pszIndice.encode('ascii'), pszValor.encode('ascii'))

		def iCNFCancelarUltimoItem_ECF_Daruma(self):
		 	return iCNFCancelarUltimoItem_ECF_Daruma()

		def iCNFCancelarItem_ECF_Daruma(self, pszNumItem):
		 	return iCNFCancelarItem_ECF_Daruma(pszNumItem.encode('ascii'))

		def iCNFCancelarDescontoItem_ECF_Daruma(self, pszNumItem):
		 	return iCNFCancelarDescontoItem_ECF_Daruma(pszNumItem.encode('ascii'))

		def iCNFCancelarDescontoUltimoItem_ECF_Daruma(self):
		 	return iCNFCancelarDescontoUltimoItem_ECF_Daruma()

		def iCNFCancelarAcrescimoItem_ECF_Daruma(self, pszNumItem):
		 	return iCNFCancelarAcrescimoItem_ECF_Daruma(pszNumItem.encode('ascii'))

		def iCNFCancelarAcrescimoUltimoItem_ECF_Daruma(self):
		 	return iCNFCancelarAcrescimoUltimoItem_ECF_Daruma()

		def iCNFTotalizarComprovante_ECF_Daruma(self, pszTipoDescAcresc, pszValorDescAcresc):
		 	return iCNFTotalizarComprovante_ECF_Daruma(pszTipoDescAcresc.encode('ascii'), pszValorDescAcresc.encode('ascii'))

		def iCNFTotalizarComprovantePadrao_ECF_Daruma(self):
		 	return iCNFTotalizarComprovantePadrao_ECF_Daruma()

		def iCNFCancelarDescontoSubtotal_ECF_Daruma(self):
		 	return iCNFCancelarDescontoSubtotal_ECF_Daruma()

		def iCNFCancelarAcrescimoSubtotal_ECF_Daruma(self):
		 	return iCNFCancelarAcrescimoSubtotal_ECF_Daruma()

		def iCNFEfetuarPagamento_ECF_Daruma(self, pszFormaPgto, pszValor, pszInfoAdicional):
		 	return iCNFEfetuarPagamento_ECF_Daruma(
		 		pszFormaPgto.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszInfoAdicional.encode('ascii')
		 	)

		def iCNFEfetuarPagamentoFormatado_ECF_Daruma(self, psszFormaPgto, pszValor):
		 	return iCNFEfetuarPagamentoFormatado_ECF_Daruma(psszFormaPgto.encode('ascii'), pszValor.encode('ascii'))

		def iCNFEfetuarPagamentoPadrao_ECF_Daruma(self):
		 	return iCNFEfetuarPagamentoPadrao_ECF_Daruma()

		def iCNFEncerrar_ECF_Daruma(self, pszMensagem):
		 	return iCNFEncerrar_ECF_Daruma(pszMensagem.encode('ascii'))

		def iCNFEncerrarPadrao_ECF_Daruma(self):
		 	return iCNFEncerrarPadrao_ECF_Daruma()

		def iCNFCancelar_ECF_Daruma(self):
		 	return iCNFCancelar_ECF_Daruma()

		# Configuracoes da Impressora Fiscal
		def confCadastrar_ECF_Daruma(self, pszCadastrar, pszValor, pszSeparador):
		 	return confCadastrar_ECF_Daruma(
		 		pszCadastrar.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszSeparador.encode('ascii')
		 	)

		def confCadastrarPadrao_ECF_Daruma(self, pszCadastrar, pszValor):
		 	return confCadastrarPadrao_ECF_Daruma(pszCadastrar.encode('ascii'), pszValor.encode('ascii'))

		def confDesabilitarHorarioVerao_ECF_Daruma(self):
		 	return confDesabilitarHorarioVerao_ECF_Daruma()

		def confDesabilitarModoPreVenda_ECF_Daruma(self):
		 	return confDesabilitarModoPreVenda_ECF_Daruma()

		def confHabilitarHorarioVerao_ECF_Daruma(self):
		 	return confHabilitarHorarioVerao_ECF_Daruma()

		def confHabilitarModoPreVenda_ECF_Daruma(self):
		 	return confHabilitarModoPreVenda_ECF_Daruma()

		def confProgramarAvancoPapel_ECF_Daruma(self, pszSepEntreLinhas, pszSepEntreDoc, pszLinhasGuilhotina, pszGuilhotina, pszImpClicheAntecipada):
		 	return confProgramarAvancoPapel_ECF_Daruma(
		 		pszSepEntreLinhas.encode('ascii'),
		 		pszSepEntreDoc.encode('ascii'),
		 		pszLinhasGuilhotina.encode('ascii'),
		 		pszGuilhotina.encode('ascii'),
		 		pszImpClicheAntecipada.encode('ascii')
		 	)

		def confProgramarIDLoja_ECF_Daruma(self, pszValor):
		 	return confProgramarIDLoja_ECF_Daruma(pszValor.encode('ascii'))

		def confProgramarOperador_ECF_Daruma(self, pszValor):
		 	return confProgramarOperador_ECF_Daruma(pszValor.encode('ascii'))

		# Cupom Fiscal
		def iCFAbrir_ECF_Daruma(self, pszCPF, pszNome, pszEndereco):
		 	return iCFAbrir_ECF_Daruma(
		 		pszCPF.encode('ascii'), 
		 		pszNome.encode('ascii'), 
		 		pszEndereco.encode('ascii')
		 	)

		def iCFAbrirPadrao_ECF_Daruma(self):
		 	return iCFAbrirPadrao_ECF_Daruma()

		def iCFVender_ECF_Daruma(self, pszCargaTributaria, pszQuantidade, pszPrecoUnitario, pszTipoDescAcresc, pszValorDescAcresc, pszCodigoItem, pszUnidadeMedida, pszDescricaoItem):
		 	return iCFVender_ECF_Daruma(
		 		pszCargaTributaria.encode('ascii'),
		 		pszQuantidade.encode('ascii'),
		 		pszPrecoUnitario.encode('ascii'),
		 		pszTipoDescAcresc.encode('ascii'),
		 		pszValorDescAcresc.encode('ascii'),
		 		pszCodigoItem.encode('ascii'),
		 		pszUnidadeMedida.encode('ascii'),
		 		pszDescricaoItem.encode('ascii')
		 	)

		def iCFVenderResumido_ECF_Daruma(self, pszCargaTributaria, pszPrecoUnitario, pszCodigoItem, pszDescricaoItem):
		 	return iCFVenderResumido_ECF_Daruma(
		 		pszCargaTributaria.encode('ascii'),
		 		pszPrecoUnitario.encode('ascii'),
		 		pszCodigoItem.encode('ascii'),
		 		pszDescricaoItem.encode('ascii')
		 	)

		def iCFVenderSemDesc_ECF_Daruma(self, pszCargaTributaria, pszQuantidade, pszPrecoUnitario, pszCodigoItem, pszUnidadeMedida, pszDescricaoItem):
		 	return iCFVenderSemDesc_ECF_Daruma(
		 		pszCargaTributaria.encode('ascii'),
		 		pszQuantidade.encode('ascii'),
		 		pszPrecoUnitario.encode('ascii'),
		 		pszCodigoItem.encode('ascii'),
		 		pszUnidadeMedida.encode('ascii'),
		 		pszDescricaoItem.encode('ascii')
		 	)

		def iCFLancarDescontoItem_ECF_Daruma(self, pszNumItem, pszTipoDesc, pszValorDesc):
		 	return iCFLancarDescontoItem_ECF_Daruma(
		 		pszNumItem.encode('ascii'),
		 		pszTipoDesc.encode('ascii'),
		 		pszValorDesc.encode('ascii')
		 	)

		def iCFLancarAcrescimoItem_ECF_Daruma(self, pszNumItem, pszTipoAcresc, pszValorAcresc):
		 	return iCFLancarAcrescimoItem_ECF_Daruma(
		 		pszNumItem.encode('ascii'),
		 		pszTipoAcresc.encode('ascii'),
		 		pszValorAcresc.encode('ascii')
		 	)

		def iCFLancarDescontoUltimoItem_ECF_Daruma(self, pszTipoDesc, pszValorDesc):
		 	return iCFLancarDescontoUltimoItem_ECF_Daruma(pszTipoDesc.encode('ascii'), pszValorDesc.encode('ascii'))

		def iCFLancarAcrescimoUltimoItem_ECF_Daruma(self, pszTipoAcresc, pszValorAcresc):
		 	return iCFLancarAcrescimoUltimoItem_ECF_Daruma(pszTipoAcresc.encode('ascii'), pszValorAcresc.encode('ascii'))

		def iCFCancelarItem_ECF_Daruma(self, pszNumItem):
		 	return iCFCancelarItem_ECF_Daruma(pszNumItem..encode('ascii'))

		def iCFCancelarDescontoItem_ECF_Daruma(self, pszNumItem):
		 	return iCFCancelarDescontoItem_ECF_Daruma(pszNumItem.encode('ascii'))

		def iCFCancelarDescontoUltimoItem_ECF_Daruma(self):
		 	return iCFCancelarDescontoUltimoItem_ECF_Daruma()

		def iCFCancelarAcrescimoItem_ECF_Daruma(self, pszNumItem):
		 	return iCFCancelarAcrescimoItem_ECF_Daruma(pszNumItem.encode('ascii'))

		def iCFCancelarAcrescimoUltimoItem_ECF_Daruma(self):
		 	return iCFCancelarAcrescimoUltimoItem_ECF_Daruma()

		def iCFCancelarDescontoSubtotal_ECF_Daruma(self):
		 	return iCFCancelarDescontoSubtotal_ECF_Daruma()

		def iCFCancelarAcrescimoSubtotal_ECF_Daruma(self):
		 	return iCFCancelarAcrescimoSubtotal_ECF_Daruma()

		def iCFCancelarItemParcial_ECF_Daruma(self, pszNumItem, pszQuantidade):
		 	return iCFCancelarItemParcial_ECF_Daruma(pszNumItem.encode('ascii'), pszQuantidade.encode('ascii'))

		def iCFCancelarUltimoItem_ECF_Daruma(self):
		 	return iCFCancelarUltimoItem_ECF_Daruma()

		def iCFCancelarUltimoItemParcial_ECF_Daruma(self, pszQuantidade):
		 	return iCFCancelarUltimoItemParcial_ECF_Daruma(pszQuantidade.encode('ascii'))

		def iCFTotalizarCupom_ECF_Daruma(self, pszTipoDescAcresc, pszValorDescAcresc):
		 	return iCFTotalizarCupom_ECF_Daruma(pszTipoDescAcresc.encode('ascii'), pszValorDescAcresc.encode('ascii'))

		def iCFTotalizarCupomPadrao_ECF_Daruma(self):
		 	return iCFTotalizarCupomPadrao_ECF_Daruma()

		def iCFEfetuarPagamento_ECF_Daruma(self, psszFormaPgto, pszValor, pszInfoAdicional):
		 	return iCFEfetuarPagamento_ECF_Daruma(
		 		psszFormaPgto.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszInfoAdicional.encode('ascii')
		 	)

		def iCFEfetuarPagamentoFormatado_ECF_Daruma(self, pszFormaPgto, pszValor):
		 	return iCFEfetuarPagamentoFormatado_ECF_Daruma(pszFormaPgto.encode('ascii'), pszValor.encode('ascii'))

		def iCFEfetuarPagamentoPadrao_ECF_Daruma(self):
		 	return iCFEfetuarPagamentoPadrao_ECF_Daruma()

		def iEstornarPagamento_ECF_Daruma(self, pszFormaPgtoEstornado, pszFormaPgtoEfetivado, pszValor, pszInfoAdicional):
		 	return iEstornarPagamento_ECF_Daruma(
		 		pszFormaPgtoEstornado.encode('ascii'),
		 		pszFormaPgtoEfetivado.encode('ascii'),
		 		pszValor.encode('ascii'),
		 		pszInfoAdicional.encode('ascii'))

		def iCFIdentificarConsumidor_ECF_Daruma(self, pszNome, pszEndereco, pszCPF):
		 	return iCFIdentificarConsumidor_ECF_Daruma(
		 		pszNome.encode('ascii'),
		 		pszEndereco.encode('ascii'),
		 		pszCPF.encode('ascii')
		 	)

		def iCFEncerrar_ECF_Daruma(self, pszCupomAdicional, pszMensagem):
		 	return iCFEncerrar_ECF_Daruma(pszCupomAdicional.encode('ascii'), pszMensagem.encode('ascii'))

		def iCFEncerrarConfigMsg_ECF_Daruma(self, pszMensagem):
		 	return iCFEncerrarConfigMsg_ECF_Daruma(pszMensagem.encode('ascii'))

		def iCFEncerrarPadrao_ECF_Daruma(self):
		 	return iCFEncerrarPadrao_ECF_Daruma()

		def iCFEncerrarResumido_ECF_Daruma(self):
		 	return iCFEncerrarResumido_ECF_Daruma()

		def iCFCancelar_ECF_Daruma(self):
		 	return iCFCancelar_ECF_Daruma()

		def iCFEmitirCupomAdicional_ECF_Daruma(self):
		 	return iCFEmitirCupomAdicional_ECF_Daruma()

		def rCFSaldoAPagar_ECF_Daruma(self, pszValor):
		 	return rCFSaldoAPagar_ECF_Daruma(byref(pszValor.encode('ascii')))

		def rCFSubTotal_ECF_Daruma(self, pszValor):
		 	return rCFSubTotal_ECF_Daruma(byref(pszValor.encode('ascii')))

		def rCFVerificarStatus_ECF_Daruma(self, pszStatus, piStatus):
		 	return rCFVerificarStatus_ECF_Daruma(byref(pszStatus.encode('ascii')), byref(piStatus))

		def rCMEfetuarCalculo_ECF_Daruma(self, pszISS, pszICMS):
		 	return rCMEfetuarCalculo_ECF_Daruma(byref(pszISS.encode('ascii')), byref(pszICMS.encode('ascii'))

		# Gaveta Autentica Outros
		def eAbrirGaveta_ECF_Daruma():
		 	return eAbrirGaveta_ECF_Daruma(self)

		def eAcionarGuilhotina_ECF_Daruma(self, pszTipoCorte):
		 	return eAcionarGuilhotina_ECF_Daruma(pszTipoCorte.encode('ascii'))

		def eCarregarBitmapPromocional_ECF_Daruma(self, pszPathLogotipo, pszNumBitmap, pszOrientacao):
		 	return eCarregarBitmapPromocional_ECF_Daruma(
		 		pszPathLogotipo.encode('ascii'),
		 		pszNumBitmap.encode('ascii'),
		 		pszOrientacao.encode('ascii')
		 	)

		def eSinalSonoro_ECF_Daruma(self, StrNumeroBeep):
		 	return eSinalSonoro_ECF_Daruma(StrNumeroBeep.encode('ascii'))

		def rStatusGaveta_ECF_Daruma(self, Int_Status):
		 	return rStatusGaveta_ECF_Daruma(byref(Int_Status))

		#Geração de Arquivos
		def rGerarEspelhoMFD_ECF_Daruma(self, pszTipo, pszInicial, pszFinal):
		 	return rGerarEspelhoMFD_ECF_Daruma(
		 		pszTipo.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		pszFinal.encode('ascii')
		 	)

		def rGerarRelatorio_ECF_Daruma(self, szRelatorio, szTipo, pszInicial, pszFinal):
		 	return rGerarRelatorio_ECF_Daruma(
		 		szRelatorio.encode('ascii'),
		 		szTipo.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		pszFinal.encode('ascii')
		 	)

		def rGerarRelatorioOffline_ECF_Daruma(self, szRelatorio, szTipo, pszInicial, pszInicial, szArquivo_MF, szArquivo_MFD, szArquivo_INF):
		 	return rGerarRelatorioOffline_ECF_Daruma(
		 		szRelatorio.encode('ascii'),
		 		szTipo.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		szArquivo_MF.encode('ascii'),
		 		szArquivo_MFD.encode('ascii'),
		 		szArquivo_INF.encode('ascii')
		 	)

		def rGerarMapaResumo(self):
		 	return rGerarMapaResumo()

		def rEfetuarDownloadMFD_ECF_Daruma(self, pszTipo, pszInicial, pszFinal, pszNomeArquivo):
		 	return rEfetuarDownloadMFD_ECF_Daruma(
		 		pszTipo.encode('ascii'),
		 		pszInicial.encode('ascii'),
		 		pszFinal.encode('ascii'),
		 		pszNomeArquivo.encode('ascii')
		 	)

		def rEfetuarDownloadMF_ECF_Daruma(self, pszNomeArquivo):
		 	return rEfetuarDownloadMF_ECF_Daruma(pszNomeArquivo.encode('ascii'))

		# Lei DE OLHO no Imposto
		def confCFNCM_ECF_Daruma(self, pszNCM, pszTipoOrigem):
		 	return confCFNCM_ECF_Daruma(pszNCM.encode('ascii'), pszTipoOrigem.encode('ascii'))

		def rCFVrImposto_ECF_Daruma(self, pszNumeroItem, pszVrImposto):
		 	return rCFVrImposto_ECF_Daruma(pszNumeroItem.encode('ascii'), pszVrImposto.encode('ascii'))

		# PAF-ECF
		def ePAFCadastrar_ECF_Daruma(self, pszNomeArquivo, pszChave, pszNumSerieECF, pszGT):
		 	return ePAFCadastrar_ECF_Daruma(
		 		pszNomeArquivo.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszNumSerieECF.encode('ascii'),
		 		pszGT.encode('ascii')
		 	)

		def ePAFValidarDados_ECF_Daruma(self, pszNomeArquivo, pszChave, pszNumSerieEFC, pszGT):
		 	return ePAFValidarDados_ECF_Daruma(
		 		pszNomeArquivo.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszNumSerieEFC.encode('ascii'),
		 		pszGT.encode('ascii')
		 	)

		def ePAFAtualizarGT_ECF_Daruma(self, pszNomeArquivo, pszChave, pszNumSerieECF, pszGT):
		 	return ePAFAtualizarGT_ECF_Daruma(
		 		pszNomeArquivo.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszNumSerieECF.encode('ascii'),
		 		pszGT.encode('ascii')
		 	)

		def confModoPAF_ECF_Daruma(self, pszAtivar, pszChave, pszNomeArquivo):
		 	return confModoPAF_ECF_Daruma(
		 		pszAtivar.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszNomeArquivo.encode('ascii')
		 	)

		def rLerArqRegistroPAF_ECF_Daruma(self, pszCaminho, pszChave, pszReturn):
		 	return rLerArqRegistroPAF_ECF_Daruma(
		 		pszCaminho.encode('ascii'),
		 		pszChave.encode('ascii'),
		 		pszReturn.encode('ascii')
		 	)

		def eRSAAssinarArquivo(self, szArquivo, szChavePrivada):
		 	return eRSAAssinarArquivo(szArquivo.encode('ascii'), szChavePrivada.encode('ascii'))

		def rAssinarRSA_ECF_Daruma(self, pszPathArquivo, pszChavePrivada, pszAssinaturaGerada):
		 	return rAssinarRSA_ECF_Daruma(
		 		pszPathArquivo.encode('ascii'),
		 		pszChavePrivada.encode('ascii'),
		 		pszAssinaturaGerada.encode('ascii')
		 	)

		def rRSAChavePublica(self, szChavePrivada, szChavePublica, szExpoenteszExpoente):
		 	return rRSAChavePublica(
		 		szChavePrivada.encode('ascii'),
		 		szChavePublica.encode('ascii'),
		 		szExpoenteszExpoente.encode('ascii')
		 	)

		def rCalcularMD5_ECF_Daruma(self, pszPathArquivo, pszMD5GeradoHex, pszMD5GeradoAscii):
		 	return rCalcularMD5_ECF_Daruma(
		 		pszPathArquivo.encode('ascii'),
		 		pszMD5GeradoHex.encode('ascii'),
		 		pszMD5GeradoAscii.encode('ascii')
		 	)

		def rCodigoModeloFiscal_ECF_Daruma(self, pszValor):
		 	return rCodigoModeloFiscal_ECF_Daruma(pszValor.encode('ascii'))

		def rRetornarGTCodificado_ECF_Daruma(self, pszValor):
		 	return rRetornarGTCodificado_ECF_Daruma(pszValor.encode('ascii'))

		def rRetornarNumeroSerieCodificado_ECF_Daruma(self, pszValor):
		 	return rRetornarNumeroSerieCodificado_ECF_Daruma(pszValor.encode('ascii'))

		def rVerificarGTCodificado_ECF_Daruma(self, pszValor):
		 	return rVerificarGTCodificado_ECF_Daruma(pszValor.encode('ascii'))

		def rVerificarNumeroSerieCodificado_ECF_Daruma(self, pszValor):
		 	return rVerificarNumeroSerieCodificado_ECF_Daruma(pszValor.encode('ascii'))

		def eMemoriaFiscal_ECF_Daruma(self, pszInicial, pszFinal, pszCompleta, pszTipo):
		 	return eMemoriaFiscal_ECF_Daruma(
		 		pszInicial.encode('ascii'),
		 		pszFinal.encode('ascii'),
		 		pszCompleta.encode('ascii'),
		 		pszTipo.encode('ascii')
		 	)

		# Registry
		def regCFCupomAdicionalDllConfig_ECF_Daruma(self, pszParametro):
		 	return regCFCupomAdicionalDllConfig_ECF_Daruma(pszParametro.encode('ascii'))

		def regSintegra_ECF_Daruma(self, pszPathChave, pszValor):
		 	return regSintegra_ECF_Daruma(pszPathChave.encode('ascii'), pszValor.encode('ascii'))

		# Relatorio Gerencial
		def iRGAbrir_ECF_Daruma(self, pszNomeRG):
		 	return iRGAbrir_ECF_Daruma(pszNomeRG.encode('ascii'))

		def iRGAbrirIndice_ECF_Daruma(self, pszIndiceRG):
		 	return iRGAbrirIndice_ECF_Daruma(pszIndiceRG)

		def iRGAbrirPadrao_ECF_Daruma(self, pszTexto):
		 	return iRGAbrirPadrao_ECF_Daruma(pszTexto.encode('ascii'))

		def iRGImprimirTexto_ECF_Daruma(self, pszArquivo):
		 	return iRGImprimirTexto_ECF_Daruma(pszArquivo.encode('ascii'))

		def iRGImprimirArquivo_ECF_Daruma(self):
		 	return iRGImprimirArquivo_ECF_Daruma()

		def iRGFechar_ECF_Daruma(self):
		 	return iRGFechar_ECF_Daruma()

		def rRGVerificarStatus_ECF_Daruma(self, pszStatus):
		 	return rRGVerificarStatus_ECF_Daruma(byref(pszStatus.encode('ascii')))

		# Relatorios Fiscais
		def iLeituraX_ECF_Daruma(self):
			return iLeituraX_ECF_Daruma()

		def rLeituraX_ECF_Daruma(self):
		 	return rLeituraX_ECF_Daruma()

		def rLeituraXCustomizada_ECF_Daruma(self, pszCaminho):
		 	return rLeituraXCustomizada_ECF_Daruma(pszCaminho.encode('ascii'))

		def iMFLer_ECF_Daruma(self, pszInicial, pszFinal):
		 	return iMFLer_ECF_Daruma(pszInicial.encode('ascii'), pszFinal.encode('ascii'))

		def iMFLerSerial_ECF_Daruma(self, pszInicial, pszFinal):
		 	return iMFLerSerial_ECF_Daruma(pszInicial.encode('ascii'), pszFinal.encode('ascii'))

		def iSangria_ECF_Daruma(self, pszValor, pszMensagem):
		 	return iSangria_ECF_Daruma(pszValor.encode('ascii'), pszMensagem.encode('ascii'))

		def iSangriaPadrao_ECF_Daruma(self):
		 	return iSangriaPadrao_ECF_Daruma()

		def iSuprimento_ECF_Daruma(self, pszValor, pszMensagem):
		 	return iSuprimento_ECF_Daruma(pszValor.encode('ascii'), pszMensagem.encode('ascii'))

		def iSuprimentoPadrao_ECF_Daruma(self):
		 	return iSuprimentoPadrao_ECF_Daruma()

		def iRelatorioConfiguracao_ECF_Daruma(self):
		 	return iRelatorioConfiguracao_ECF_Daruma()

		def iReducaoZ_ECF_Daruma(self, pszData, pszHora):
			return iReducaoZ_ECF_Daruma(pszData.encode('ascii'), pszHora.encode('ascii'))

		# Retornos e Status
		def eBuscarPortaVelocidade_ECF_Daruma(self):
		 	return eBuscarPortaVelocidade_ECF_Daruma()

		def eRetornarPortasCOM_ECF_Daruma(self, pszRetorno):
		 	return eRetornarPortasCOM_ECF_Daruma(byref(pszRetorno.encode('ascii')))

		def eInterpretarRetorno_ECF_Daruma(self, iIndice, pszRetorno):
		 	return eInterpretarRetorno_ECF_Daruma(iIndice, pszRetorno.encode('ascii'))

		def eInterpretarAviso_ECF_Daruma(self, iIndice, pszRetorno):
		 	return eInterpretarAviso_ECF_Daruma(iIndice, pszRetorno.encode('ascii'))

		def eInterpretarErro_ECF_Daruma(self, iIndice, pszRetorno):
		 	return eInterpretarErro_ECF_Daruma(iIndice, pszRetorno.encode('ascii'))

		def eRetornarAvisoErroUltimoCMD_ECF_Daruma(self, Str_Aviso, Str_Erro):
		 	return eRetornarAvisoErroUltimoCMD_ECF_Daruma(Str_Aviso.encode('ascii'), Str_Erro.encode('ascii'))

		def rStatusImpressora_ECF_Daruma(self, pszStatus):
		 	return rStatusImpressora_ECF_Daruma(byref(pszStatus.encode('ascii')))

		def rStatusImpressoraBinario_ECF_Daruma(self, pszStatus):
		 	return rStatusImpressoraBinario_ECF_Daruma(byref(pszStatus.encode('ascii')))

		def rConsultaStatusImpressoraInt_ECF_Daruma(self, iIndice, iRetorno):
		 	return rConsultaStatusImpressoraInt_ECF_Daruma(iIndice, byref(iRetorno))

		def rConsultaStatusImpressoraStr_ECF_Daruma(self, iIndice, szStatus):
		 	return rConsultaStatusImpressoraStr_ECF_Daruma(iIndice, byref(szStatus))

		def rStatusUltimoCmd_ECF_Daruma(self, pszErro, pszAviso, piErro, piAviso):
		 	return rStatusUltimoCmd_ECF_Daruma(
		 		byref(pszErro.encode('ascii')),
		 		byref(pszAviso.encode('ascii')),
		 		byref(piErro),
		 		byref(piAviso))

		def rStatusUltimoCMDInt_ECF_Daruma(self, iErro, iAviso):
		 	return rStatusUltimoCMDInt_ECF_Daruma(byref(iErro), byref(iAviso))

		def rStatusUltimoCmdStr_ECF_Daruma(self, pszErro, pszAviso):
		 	return rStatusUltimoCmdStr_ECF_Daruma(byref(pszErro.encode('ascii')), byref(pszAviso.encode('ascii')))

		def rInfoEstendida_ECF_Daruma(self, indice, pszRetorno):
		 	return rInfoEstendida_ECF_Daruma(indice, byref(pszRetorno.encode('ascii')))

		def rInfoEstendida1_ECF_Daruma(self, pszInfo1):
		 	return rInfoEstendida1_ECF_Daruma(byref(pszInfo1.encode('ascii')))

		def rInfoEstendida2_ECF_Daruma(self, pszInfo2):
		 	return rInfoEstendida2_ECF_Daruma(byref(pszInfo2.encode('ascii')))

		def rInfoEstendida3_ECF_Daruma(self, pszInfo3):
		 	return rInfoEstendida3_ECF_Daruma(byref(pszInfo3.encode('ascii')))

		def rInfoEstendida4_ECF_Daruma(self, pszInfo4):
		 	return rInfoEstendida4_ECF_Daruma(byref(pszInfo4.encode('ascii')))

		def rInfoEstendida5_ECF_Daruma(self, pszInfo5):
		 	return rInfoEstendida5_ECF_Daruma(byref(pszInfo5.encode('ascii')))

		def rRetornarInformacao_ECF_Daruma(self, pszIndice, pszRetornar):
		 	return rRetornarInformacao_ECF_Daruma(pszIndice.encode('ascii'), byref(pszRetornar.encode('ascii')))

		def rRetornarInformacaoSeparador_ECF_Daruma(self, pszIndice, pszVSignificativo, pszRetornar):
		 	return rRetornarInformacaoSeparador_ECF_Daruma(
		 		pszIndice.encode('ascii'), 
		 		pszVSignificativo.encode('ascii'), 
		 		byref(pszRetornar.encode('ascii')
		 	)

		def rLerAliquotas_ECF_Daruma(self, cAliquotas):
		 	return rLerAliquotas_ECF_Daruma(byref(cAliquotas.encode('ascii')))

		def rLerMeiosPagto_ECF_Daruma(self, pszRelatorios):
		 	return rLerMeiosPagto_ECF_Daruma(byref(pszRelatorios.encode('ascii')))

		def rLerRG_ECF_Daruma(self, pszRelatorios):
		 	return rLerRG_ECF_Daruma(byref(pszRelatorios.encode('ascii')))

		def rLerCNF_ECF_Daruma(self, pszTotalizadores):
		 	return rLerCNF_ECF_Daruma(byref(pszTotalizadores.encode('ascii')))

		def rInfoCNF_ECF_Daruma(self, pszRetorno):
		 	return rInfoCNF_ECF_Daruma(byref(pszRetorno.encode('ascii')))

		def rLerDecimais_ECF_Daruma(self, pszDecimalQtde, pszDecimalValor, piDecimalQtde, piDecimalValor):
		 	return rLerDecimais_ECF_Daruma(
		 		byref(pszDecimalQtde.encode('ascii')),
		 		byref(pszDecimalValor.encode('ascii')),
		 		byref(piDecimalQtde),
		 		byref(piDecimalValor)
		 	)

		def rLerDecimaisInt_ECF_Daruma(self, piDecimalQtde, piDecimalValor):
		 	return rLerDecimaisInt_ECF_Daruma(byref(piDecimalQtde), byref(piDecimalValor))

		def rLerDecimaisStr_ECF_Daruma(self, pszDecimalQtde, pszDecimalValor):
		 	return rLerDecimaisStr_ECF_Daruma(byref(piDecimalQtde.encode('ascii')), byref(piDecimalValor.encode('ascii')))

		def rCompararDataHora_ECF_Daruma(self, iDiferenca):
		 	return rCompararDataHora_ECF_Daruma(byref(iDiferenca))

		def rDataHoraImpressora_ECF_Daruma(self, pszData, pszHora):
		 	return rDataHoraImpressora_ECF_Daruma(byref(pszData.encode('ascii')), byref(pszHora.encode('ascii')))

		def rVerificarImpressoraLigada_ECF_Daruma(self):
		 	return rVerificarImpressoraLigada_ECF_Daruma()

		def rVerificarReducaoZ_ECF_Daruma(self, pszPendente):
		 	return rVerificarReducaoZ_ECF_Daruma(byref(pszPendente.encode('ascii')))

		def rRetornarDadosReducaoZ_ECF_Daruma(self, pszRetorno):
		 	return rRetornarDadosReducaoZ_ECF_Daruma(byref(pszRetorno.encode('ascii')))

		def rTipoUltimoDocumentoInt_ECF_Daruma(self, iDoc):
		 	return rTipoUltimoDocumentoInt_ECF_Daruma(byref(iDoc))

		def rTipoUltimoDocumentoStr_ECF_Daruma(self, pszDoc):
		 	return rTipoUltimoDocumentoStr_ECF_Daruma(byref(pszDoc.encode('ascii')))

		def rUltimoCMDEnviado_ECF_Daruma(self, pszComando):
		 	return rUltimoCMDEnviado_ECF_Daruma(byref(pszComando.encode('ascii')))

		def rMinasLegal_ECF_Daruma(self, pszRetorno):
		 	return rMinasLegal_ECF_Daruma(byref(pszRetorno.encode('ascii')))

		def rRetornarVendaBruta_ECF_Daruma(self, pszRetorno):
		 	return rRetornarVendaBruta_ECF_Daruma(byref(pszRetorno.encode('ascii')))

		def rRetornarVendaLiquida_ECF_Daruma(self, pszVendaLiquida):
		 	return rRetornarVendaLiquida_ECF_Daruma(byref(pszVendaLiquida.encode('ascii')))

		def rCFSaldoAPagar_ECF_Daruma(self, pszValor):
		 	return rCFSaldoAPagar_ECF_Daruma(byref(pszValor.encode('ascii')))

		def rCFSubTotal_ECF_Daruma(self, pszValor):
		 	return rCFSubTotal_ECF_Daruma(byref(pszValor.encode('ascii')))

		# WebService
		def eWsEnviarCupom_ECF_Daruma(self, pszCPF, pszNomeFantasia, pszIndiceSegmento, pszCCF, pszData, pszHora, pszValor, pszISS, pszICMS, szReservado, iRespostaWS):
		 	return eWsEnviarCupom_ECF_Daruma(
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
		 		byref(iRespostaWS)

		def eWsStatus_ECF_Daruma(self, iRespostaWS):
		 	return eWsStatus_ECF_Daruma(byref(iRespostaWS))

ECF = DarumaFramework()