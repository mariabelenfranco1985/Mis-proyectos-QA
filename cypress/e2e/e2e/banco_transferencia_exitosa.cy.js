describe('Prueba de transferencia bancaria exitosa', () => {

  it('Debe permitir transferir dinero entre cuentas del mismo usuario', () => {
    cy.visit('https://parabank.parasoft.com/')

    // Paso 1: iniciar sesión con usuario válido
    cy.get('input[name="username"]').type('john')
    cy.get('input[name="password"]').type('demo')
    cy.get('input[value="Log In"]').click()

    // Paso 2: ingresar a la sección de transferencia
    cy.contains('Transfer Funds').click()

    // Paso 3: completar los datos de transferencia
    cy.get('input[id="amount"]').type('50')
    cy.get('select[id="fromAccountId"]').select(0)
    cy.get('select[id="toAccountId"]').select(1)
    cy.get('input[value="Transfer"]').click()

    // Paso 4: verificar mensaje de confirmación
    cy.get('#rightPanel')
      .should('contain.text', 'Transfer Complete!')
  })
})
