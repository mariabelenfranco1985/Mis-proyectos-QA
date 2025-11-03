describe('Smoke Test - Validar carga de la página principal', () => {
  it('Debería abrir la página de SauceDemo correctamente', () => {
    cy.visit('https://www.saucedemo.com/')
    cy.title().should('include', 'Swag Labs')
    cy.get('[data-test="username"]').should('be.visible')
    cy.get('[data-test="login-button"]').should('be.visible')
    cy.log('✅ Página cargada correctamente y elementos visibles.')
  })
})

