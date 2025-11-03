describe('Prueba de transferencia bancaria con monto elevado (sin validación de fondos)', () => {

  it('Debe mostrar un resultado al intentar transferir un monto muy alto', () => {
    cy.visit('https://parabank.parasoft.com/')

    // Paso 1: iniciar sesión
    cy.get('input[name="username"]').type('john')
    cy.get('input[name="password"]').type('demo')
    cy.get('input[value="Log In"]').click()

    // Paso 2: ir a Transfer Funds
    cy.contains('Transfer Funds').click()

    // Paso 3: ingresar un monto exagerado
    cy.get('#amount').type('9999999')
    cy.get('#fromAccountId').select(0)
    cy.get('#toAccountId').select(1)
    cy.get('input[value="Transfer"]').click()

    // Paso 4: capturar el texto del panel y verificar resultado
    cy.get('#rightPanel').then(($panel) => {
      const texto = $panel.text()

      if (texto.includes('Transfer Complete!')) {
        expect(texto).to.include('Transfer Complete!')
        console.log('✅ El sitio permitió la transferencia (entorno de prueba).')
      } 
      else if (texto.includes('could not be completed') || texto.includes('Error')) {
        console.log('⚠️ El sitio mostró error esperado en la transferencia.')
      } 
      else {
        throw new Error('❌ No se mostró ningún mensaje claro después de la transferencia.')
      }
    })
  })
})
